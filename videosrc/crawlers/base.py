import os
import logging

from abc import ABC
from datetime import datetime, timedelta

from videosrc.models import Channel, Video, VideoSource
from videosrc.errors import InvalidOptionError
from videosrc.utils import aenumerate


VIDEOSRC_PROXY = os.getenv('VIDEOSRC_PROXY', None)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class Crawler(ABC):
    auth_fields = {}

    def __init__(self, state=None, save_state=None, proxy=VIDEOSRC_PROXY,
                 ChannelModel=Channel, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self._state = state
        self._save_state = save_state
        self._proxy = proxy
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        raise NotImplementedError()

    def save_state(self):
        if not callable(self._save_state):
            LOGGER.info('No state saving function')
            return
        self._save_state(self._state)

    async def login(self, *args, **kwargs):
        raise NotImplementedError()

    async def _iter_videos(self, *args, **kwargs):
        raise NotImplementedError()

    async def iter_videos(self, *args, **kwargs):
        now = datetime.now()
        max_count = kwargs.pop('max_count', None)
        try:
            max_days = int(kwargs['max_days'])
            max_days = datetime.now() - timedelta(days=max_days)

        except ValueError:
            raise InvalidOptionError('max_days should be an int')

        except KeyError:
            max_days = None

        async for i, video in aenumerate(self._iter_videos(*args, **kwargs)):
            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

            else:
                if max_count is not None and i >= max_count:
                    LOGGER.info('Reached max item count')
                    break
                if max_days is not None and now <= max_days:
                    LOGGER.info('Reached max item age')
                    break

        self.save_state()

    async def crawl(self, url, **kwargs):
        return await self._crawl(url, **kwargs)
