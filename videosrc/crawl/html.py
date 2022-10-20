import logging

from urllib.parse import urljoin
from hashlib import md5
from email.utils import parsedate_to_datetime

from aiohttp.hdrs import METH_GET
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.models import Channel, Video, VideoSource
from videosrc.utils import dict_repr, url2title, MediaInfo, basic_auth


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class HTMLCrawler:
    def __init__(self, state=None, ChannelModel=Channel, VideoModel=Video,
                 VideoSourceModel=VideoSource):
        self.auth = {}
        self.state = state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        # NOTE: This crawler is too generalized to claim a url. It will be
        # chosen as a default if no other crawler claims a url.
        return False

    async def login(self, username, password):
        self.auth = basic_auth(username, password)

    async def _iter_videos(self, url, soup):
        for a in soup.find_all('a'):
            # NOTE: Link might be absolute.
            href = urljoin(url, a['href'])
            info = MediaInfo(href)
            source = self.VideoSourceModel(
                width=info.frame.width,
                height=info.frame.height,
                fps=info.stream.guessed_rate,
                size=info.size,
                url=href,
                original={
                    'url': href,
                    'video': dict_repr(info.video),
                },
            )
            video = self.VideoModel(
                extern_id=md5(href.encode()).hexdigest(),
                title=url2title(href),
                poster=info.poster(),
                duration=info.stream.duration,
                published=info.last_modified(),
                sources=[source],
                original={
                    'url': href,
                    'tag': str(a),
                    'headers': dict(info.headers),
                },
            )
            yield video, self.state

    async def crawl(self, url, options=None):
        async with ScraperSession() as s:
            r = await s._request(METH_GET, url, **self.auth)
            try:
                self.state = {
                    'Last-Modified': parsedate_to_datetime(
                        r.headers['Last-Modified']),
                    'Content-Length': int(r.headers['Content-Length']),
                }
            except KeyError as e:
                LOGGER.warning(
                    'Could not read header: %s, cannot save state', e.args[0])
            soup = BeautifulSoup(await r.text(), 'html.parser')
            title = soup.find('title').text
            channel = self.ChannelModel(
                name=title,
                url=url,
            )
            return channel, self._iter_videos(url, soup)
