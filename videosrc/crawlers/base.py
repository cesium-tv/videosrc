import logging

from abc import ABC

from videosrc.models import Channel, Video, VideoSource


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class Crawler(ABC):
    def __init__(self, state=None, save_state=None, ChannelModel=Channel,
                 VideoModel=Video, VideoSourceModel=VideoSource):
        self.state = state
        self.save_state = save_state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        raise NotImplementedError()

    def on_state(self, state):
        LOGGER.debug('State update: %s', state)
        if not callable(self.save_state):
            LOGGER.info('No state saving function')
            return
        self.save_state(state)

    async def login(self, **credentials):
        raise NotImplementedError()

    async def crawl(self, url, **options):
        raise NotImplementedError()
