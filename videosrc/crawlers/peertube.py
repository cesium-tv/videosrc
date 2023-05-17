import logging
from urllib.parse import urlparse, urljoin, urlunparse
from os.path import split as pathsplit
from datetime import datetime

from aiohttp.hdrs import METH_POST
from aiohttp_scraper import ScraperSession

from videosrc.utils import md5sum, url2mime
from videosrc.crawlers.base import Crawler


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

# '2022-07-31T01:16:56.624Z'
# '2022-07-31T00:54:44.991Z'
DATETIME_FMT = '%Y-%m-%dT%H:%M:%S.%fZ'


def maybe_parse_date(s):
    if s is None:
        return None

    try:
        return datetime.strptime(s, DATETIME_FMT)

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
        channel_name = f'{pathsplit(url.path)[1]}@{urlp.netloc}:{port}'
        return urlp, channel_name


class PeerTubeCrawler(Crawler):
    auth_fields = {
        'username': 'String',
        'password': 'String',
    }

    def __init__(self, state=0, **kwargs):
        super().__init__(state=state, **kwargs)
        self.auth = {}

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        if urlp.path.startswith('/c/') and '@' in urlp.path:
            return True
        if urlp.path.startswith('/video-channels/'):
            return True

    async def _iter_videos(self, url):
        url += '/videos'
        params = {
            'count': 25,
            'sort': '-publishedAt',
            'skipCount': 'true',
        }
        if self._state:
            params['start'] = self._state
        async with ScraperSession() as s:
            results = await s.get_json(
                url, params=params, proxy=self._proxy, **self.auth
            )

        urlp = urlparse(url)
        for result in results['data']:
            url = urlunparse((
                urlp.scheme,
                urlp.netloc,
                f"/api/v1/videos/{result['shortUUID']}", '', '', ''))
            async with ScraperSession() as s:
                obj = await s.get_json(url, proxy=self._proxy, **self.auth)
            files = obj.pop('files')

            sources = []
            for file in files:
                sources.append(self.VideoSourceModel(
                    extern_id=md5sum(file['fileUrl']),
                    width=file['resolution']['id'],
                    height=None,
                    fps=file['fps'],
                    size=file['size'],
                    mime=url2mime(file['fileUrl']),
                    url=file['fileUrl'],
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

            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

            self._state += 1

    async def login(self, url, **kwargs):
        try:
            username = kwargs['username']
            password = kwargs['password']
        except KeyError:
            LOGGER.warning('No credentials, skipping login')
            return

        async with ScraperSession() as s:
            r = await s.get_json(
                urljoin(url, '/api/v1/oauth-clients/local/'),
                proxy=self._proxy)
            params = r.json()
            r = await s._request(
                METH_POST,
                urljoin(url, '/api/v1/users/token/'),
                proxy=self._proxy,
                data={
                    'client_id': params['client_id'],
                    'client_secret': params['client_secret'],
                    'grant_type': 'password',
                    'username': username,
                    'password': password,
                },
            )
            token = await r.json()
        self.auth = {
            'headers': {
                'Authorization': f"Bearer {token['access_token']}"
            }
        }

    async def crawl(self, url, **kwargs):
        await self.login(url, **kwargs)

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
            results = await s.get_json(url, proxy=self._proxy, **self.auth)

        channel = self.ChannelModel(
            extern_id=md5sum(channel_name),
            name=channel_name,
            title=results['displayName'],
            url=results['url'],
        )

        return channel, self.iter_videos(url, **kwargs)
