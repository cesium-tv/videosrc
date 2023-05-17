import logging

from urllib.parse import urljoin
from email.utils import parsedate_to_datetime

from aiohttp.hdrs import METH_GET
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.utils import dict_repr, url2title, MediaInfo, basic_auth, md5sum
from videosrc.crawlers.base import Crawler


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class HTMLCrawler(Crawler):
    auth_fields = {
        'username': 'String',
        'password': 'String',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth = {}

    @staticmethod
    def check_url(url):
        # NOTE: This crawler is too generalized to claim a url. It will be
        # chosen as a default if no other crawler claims a url.
        return False

    async def login(self, url, **kwargs):
        try:
            username = kwargs['username']
            password = kwargs['password']
        except KeyError:
            LOGGER.warning('No credentials, skipping login')
            return

        self.auth = basic_auth(username, password)

    async def _iter_videos(self, url, soup):
        for a in soup.find_all('a'):
            # NOTE: Link might be absolute.
            href = urljoin(url, a['href'])
            guid = md5sum(href)
            with MediaInfo(href) as info:
                source = self.VideoSourceModel(
                    extern_id=guid,
                    width=info.width,
                    height=info.height,
                    fps=info.fps,
                    size=info.size,
                    url=href,
                    mime=info.mime,
                    original={
                        'url': href,
                        'video': dict_repr(info.video),
                    },
                )
                video = self.VideoModel(
                    extern_id=guid,
                    title=url2title(href),
                    poster=info.poster(),
                    duration=info.duration,
                    published=info.last_modified(),
                    sources=[source],
                    original={
                        'url': href,
                        'tag': str(a),
                        'headers': dict(info.headers),
                    },
                )

            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

    async def crawl(self, url, **kwargs):
        await self.login(url, **kwargs)

        async with ScraperSession() as s:
            r = await s._request(METH_GET, url, proxy=self._proxy, **self.auth)
            try:
                state = {
                    'Last-Modified': parsedate_to_datetime(
                        r.headers['Last-Modified']),
                    'Content-Length': int(r.headers['Content-Length']),
                }
            except KeyError as e:
                LOGGER.warning(
                    'Could not read header: %s, unknown state', e.args[0])

            else:
                if self._state == state:
                    LOGGER.info('Matching state, no updates')
                    return
                else:
                    self._state = state

            soup = BeautifulSoup(await r.text(), 'html.parser')
            title = soup.find('title').text
            channel = self.ChannelModel(
                extern_id=md5sum(url),
                name=title,
                url=url,
            )
            return channel, self.iter_videos(url, soup, **kwargs)
