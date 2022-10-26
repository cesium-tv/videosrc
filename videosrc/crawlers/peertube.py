import numbers
import logging
from urllib.parse import urlparse, urljoin, urlunparse
from os.path import split as pathsplit
from datetime import datetime
from pprint import pprint

from aiohttp.hdrs import METH_GET, METH_POST
from aiohttp_scraper import ScraperSession

from videosrc.models import Channel, Video, VideoSource


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

# '2022-07-31T01:16:56.624Z'
DATETIME_FMT = '%Y-%m-%dT%H:%M:%S%z'


def maybe_parse_date(date_str):
    if date_str is None:
        return None

    try:
        return datetime.strptime(date_str, DATETIME_FMT)

    except ValueError:
        LOGGER.exception('Error parsing datetime')
        return datetime.utcnow()


def parse_channel_name(url):
    # http://cesium.tv/video-channels/btimby_channel
    # http://cesium.tv/c/btimby_channel@cesium.tv:80/videos
    urlp = urlparse(url)
    if urlp.path.startswith('/c/') and '@' in urlp.path:
        return urlp, pathsplit(urlp.path)[1]
    if urlp.path.startswith('/video-channels/'):
        port = urlp.port or 80 if urlp.scheme == 'http' else 443
        channel_name = f'{pathsplit(url.path)[1]}@{urlp.netloc}:80'
        return urlp, channel_name


class PeerTubeCrawler:
    def __init__(self, state=None, ChannelModel=Channel, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self.auth = {}
        self.state = state or 0
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        if urlp.path.startswith('/c/') and '@' in urlp.path:
            return True
        if urlp.path.startswith('/video-channels/'):
            return True

    async def _iter_videos(self, url):
        url += '/videos'
        async with ScraperSession() as s:
            results = await s.get_json(url, params={
                'start': self.state,
                'count': 25,
                'sort': '-publishedAt',
                'skipCount': 'true',
            }, **self.auth)

        urlp = urlparse(url)
        for result in results['data']:
            url = urlunparse((
                urlp.scheme,
                urlp.netloc,
                f"/api/v1/videos/{result['shortUUID']}", '', '', ''))
            async with ScraperSession() as s:
                obj = await s.get_json(url, **self.auth)
            files = obj.pop('files')

            sources = []
            for file in files:
                sources.append(self.VideoSourceModel(
                    width = file['resolution']['id'],
                    height = None,
                    fps = file['fps'],
                    size = file['size'],
                    url = file['fileUrl'],
                    original=file,
                ))

            tags = list(obj['tags'])
            tags.append(obj['category']['label'])

            video = self.VideoModel(
                extern_id=obj['uuid'],
                title=obj['name'],
                poster=urljoin(url, obj['thumbnailPath']),
                duration=obj['duration'],
                original=obj,
                published=maybe_parse_date(obj['publishedAt']),
                tags=tags,
                sources=sources,
            )

            self.state += 1
            yield video, self.state

    async def login(self, url, username, password):
        async with ScraperSession() as s:
            r = await s.get_json(urljoin(url, '/api/v1/oauth-clients/local/'))
            params = r.json()
            r = await s._request(METH_POST, urljoin(url, '/api/v1/users/token/'), data={
                'client_id': params['client_id'],
                'client_secret': params['client_secret'],
                'grant_type': 'password',
                'username': username,
                'password': password,
            })
            token = await r.json()
        self.auth = {
            'headers': {
                'Authorization': f"Bearer {token['access_token']}"
            }
        }

    async def crawl(self, url, options=None):
        urlp, channel_name = parse_channel_name(url)

        # NOTE: We are assuming the channel name is local to the instance
        # we are connected to. If this is not a safe assumption, then we
        # need to store the full channel name including host info.
        # http://cesium.tv/api/v1/video-channels/btimby_channel@cesium.tv:80/videos?start=0&count=0&sort=-publishedAt
        # http://cesium.tv/api/v1/video-channels/btimby_channel@cesium.tv:80
        url = urlunparse((
            urlp.scheme,
            urlp.netloc,
            f'api/v1/video-channels/{channel_name}', '', '', ''))

        async with ScraperSession() as s:
            results = await s.get_json(url, **self.auth)

        channel = self.ChannelModel(
            name=channel_name,
            title=results['displayName'],
            url=results['url'],
        )

        return channel, self._iter_videos(url)
