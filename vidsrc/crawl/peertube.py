import numbers
import logging
from urllib.parse import urlparse, urljoin
from datetime import datetime

import requests

from vidsrc.auth.peertube import PeerTubeAuth
from vidsrc.models import Video, VideoSource


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


class PeerTubeCrawler:
    def __init__(self, channel, options, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self.url = channel.url
        self.channel_name = channel.extern_id
        self.options = options
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    def crawl(self, state):
        auth = PeerTubeAuth(self.url).login(self.options['credentials'])

        # NOTE: We are assuming the channel name is local to the instance
        # we are connected to. If this is not a safe assumption, then we
        # need to store the full channel name including host info.
        # http://cesium.tv/api/v1/video-channels/btimby_channel@cesium.tv:80/videos?start=0&count=0&sort=-publishedAt
        # http://cesium.tv/api/v1/video-channels/btimby_channel@cesium.tv:80
        urlp = urlparse(self.url)
        port = urlp.port or 443 if urlp.scheme == 'https' else 80
        url = urljoin(
            self.url,
            f'api/v1/video-channels/{self.channel_name}@{urlp.hostname}:{port}/videos'
        )
        state = state or { 'start': 0 }

        results = requests.get(url, params={
            'start': state['start'],
            'count': 25,
            'sort': '-publishedAt',
            'skipCount': 'true',
        }, **auth).json()

        for result in results['data']:
            obj = requests.get(
                urljoin(self.url, f"/api/v1/videos/{result['shortUUID']}"),
                **auth,
            ).json()
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
                poster=urljoin(self.url, obj['thumbnailPath']),
                duration=obj['duration'],
                original=obj,
                published=maybe_parse_date(obj['publishedAt']),
                tags=tags,
                sources=sources,
            )

            state = { 'start': state['start'] + 1 }
            yield video, state
