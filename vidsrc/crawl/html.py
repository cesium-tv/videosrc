import logging

from vidsrc.auth.basic import BasicAuth


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class HTMLCrawler:
    def __init__(self, channel, options, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self.url = channel.url
        self.channel_name = channel.extern_id
        self.options = options
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    def crawl(self, state):
        auth = BasicAuth(self.url).login(self.options['credentials'])
