import os
import logging

from asgiref.sync import sync_to_async
from abc import ABC
from datetime import datetime, timedelta

from videosrc.models import Channel, Video, VideoSource
from videosrc.errors import InvalidOptionError, StateReached
from videosrc.utils import aenumerate


VIDEOSRC_PROXY = os.getenv('VIDEOSRC_PROXY', None)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class Crawler(ABC):
    auth_fields = {}

    def __init__(self, state=None, save_state=None, proxy=VIDEOSRC_PROXY,
                 ChannelModel=Channel, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self._save_state = []
        self._state = state
        self._proxy = proxy
        if save_state is not None:
            self.on_state = save_state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    def __setattr__(self, name, value):
        # NOTE: mock property with setter only.
        if name == 'on_state':
            assert callable(value), 'State saving function must be callable'
            self._save_state.append(value)
            return
        return super().__setattr__(name, value)

    @staticmethod
    def check_url(url):
        raise NotImplementedError()

    async def save_state(self):
        if len(self._save_state) == 0:
            LOGGER.info('No state saving function')
            return

        for f in self._save_state:
            # NOTE: Caller's environment may not play nicely with asyncio.
            try:
                await sync_to_async(f)(self._state)

            except Exception:
                LOGGER.exception('Error saving state when calling %s', f)

    async def login(self, *args, **kwargs):
        raise NotImplementedError()

    async def _iter_videos(self, *args, **kwargs):
        raise NotImplementedError()

    async def iter_videos(self, *args, **kwargs):
        max_count = kwargs.pop('max_count', None)

        try:
            max_days = int(kwargs['max_days'])
            max_days = datetime.now() - timedelta(days=max_days)

        except ValueError:
            raise InvalidOptionError('max_days should be an int')

        except KeyError:
            max_days = None

        try:
            async for i, video in aenumerate(self._iter_videos(*args,
                                                               **kwargs)):
                try:
                    yield video

                except Exception as e:
                    LOGGER.exception(e)

                else:
                    if max_count is not None and i >= max_count:
                        LOGGER.info('Reached max video count')
                        break
                    if max_days is not None and video.published >= max_days:
                        LOGGER.info('Reached max video age')
                        break

        except StateReached:
            LOGGER.info('Aborting, state reached', exc_info=True)

        await self.save_state()

    async def crawl(self, url, **kwargs):
        return await self._crawl(url, **kwargs)
