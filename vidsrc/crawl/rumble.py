from vidsrc.auth.rumble import RumbleAuth
from vidsrc.models import Video, VideoSource


class RumbleCrawler:
    def __init__(self, url, options, state=None,
                 VideoModel=Video, VideoSourceModel=VideoSource):
        self.url = url
        self.options = options
        self.seen = None
        if state is not None:
            self.state = state
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @property
    def state(self):
        return list(self.seen)

    @state.setter
    def state(self, value):
        self.seen = value

    def crawl(self, url):
        auth = RumbleAuth(self.url).login(options.credentials)
