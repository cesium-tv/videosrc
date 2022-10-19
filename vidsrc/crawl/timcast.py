import re
import json
import asyncio
import logging
from urllib.parse import urljoin, urlparse

import pyppeteer
from pyppeteer.errors import PyppeteerError
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from vidsrc.models import Channel, Video, VideoSource


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

RUMBLE_DOMAIN = re.compile(r'^https://rumble.com/embed/')
JSON_EXTRACT = re.compile(r'g\.f\["\w{6,7}"\]=({.*}),loaded:d\(\)')
JSON_TRIM = re.compile(r'^(.*)"path":.*,("w":.*$)')
U_FIELD = '#user_login'
P_FIELD = '#user_pass'
SUBMIT = '#wp-submit'


class LimitReached(Exception):
    def __init__(self):
        super().__init__('Limit reached')


class DepthReached(Exception):
    def __init__(self):
        super().__init__('Depth reached')


def _no_images(request):
    if request.resourceType() == 'image':
        request.abort_()
    else:
        request.continue_()



class TimcastCrawler:
    def __init__(self,  state=None, ChannelModel=Channel,
                 VideoModel=Video, VideoSourceModel=VideoSource):
        self.auth = {}
        self.seen = set()
        if state is not None:
            self.state = state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @property
    def state(self):
        return { seen: list(self.seen) }

    @state.setter
    def state(self, value):
        if isinstance(value, (set, list)):
            self.seen = set(value)
        else:
            self.seen = value['seen']

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('timcast.com')

    async def _login(self, url, credentials, headless=True, timeout=2000):
        username = credentials['username']
        password = credentials['password']

        browser = await pyppeteer.launch(
            headless=headless,
            args=[
                '--start-maximized',
                '--no-sandbox',
                '--disable-setuid-sandbox'
            ],
            ignoreHTTPSError=True,
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False
        )

        page = await browser.newPage()

        try:
            await page.setViewport({ 'width': 1366, 'height': 768 })

            LOGGER.debug('opening url: %s', url)
            await page.goto(url, timeout=timeout, waitFor='networkidle2')

            LOGGER.debug('typing')
            await page.type(U_FIELD, username)
            await page.type(P_FIELD, password)

            LOGGER.debug('clicking submit')
            await page.click(SUBMIT)

            cookieStr = []
            for cookie in await page.cookies():
                cookieStr.append(f"{cookie['name']}={cookie['value']}")
            return {'cookies': '; '.join(cookieStr)}

        finally:
            await page.close()
            await browser.close()


    async def login(self, url, credentials, headless=True, retry=3, timeout=2000):
        url = urljoin(url, '/login/')
        loop = asyncio.get_event_loop()

        for i in range(1, 1 + retry):
            try:
                LOGGER.debug('Login attempt %i', i + 1)
                self.auth = await self._login(
                    url, credentials, headless=headless, retry=retry,
                    timeout=timeout
                )

            except (PyppeteerError, asyncio.TimeoutError):
                if i == retry:
                    raise

                LOGGER.exception('Login failed, retrying')
                time.sleep(3 ** i)

    async def _iter_videos(self, url, options):
        whitelist = options.get('whitelist', [])
        limit = options.get('limit')

        seen = set()
        videos = []

        async def _handle(url, depth):
            url = url.split('#')[0]
            if depth is not None:
                if depth == 0:
                    raise DepthReached()
                depth -= 1

            if url in seen:
                LOGGER.debug('Skipping duplicate url')
                return
            LOGGER.info('URL: %s', url)
            seen.add(url)

            async with ScraperSession() as session:
                r = await session.get_html(url, **self.auth)
                LOGGER.debug('Got %i bytes', len(r))

            soup = BeautifulSoup(r, 'html.parser')

            srcSeen = set()
            for iframe in soup.find_all('iframe'):
                LOGGER.debug('Found iframe')
                src = iframe['src']
                LOGGER.info('src: %s', src)
                if src in srcSeen:
                    LOGGER.debug('Skipping duplicate iframe')
                    continue
                if not src or not RUMBLE_DOMAIN.match(src):
                    LOGGER.debug('Missing or invalid iframe src')
                    continue
                srcSeen.add(src)

                async with ScraperSession() as session:
                    r = await session.get_html(src, **self.auth)
                    LOGGER.debug('Received %i bytes', len(r))

                m = JSON_EXTRACT.search(r)
                if not m:
                    LOGGER.warn(r)
                    continue

                data = JSON_TRIM.sub(r'\1\2}', m.group(1))
                try:
                    videos.append(data)
                    yield json.loads(data)

                except (TypeError, ValueError) as e:
                    LOGGER.exception('Invalid json')
                    LOGGER.warn(data)

            for a in soup.find_all('a'):
                LOGGER.debug('Found anchor tag')
                href = a['href']
                if not href:
                    LOGGER.debug('Missing or invalid href')
                    continue

                href = urljoin(url, href)
                LOGGER.debug('href: %s', href)
                if href in seen:
                    LOGGER.debug('Skipping duplicate href')
                    continue

                if not any([re.match(p, href) for p in whitelist]):
                    LOGGER.debug('Skipping invalid href')
                    continue

                if limit is not None:
                    LOGGER.debug('Video count: %i of %i', len(videos), limit)
                    if len(videos) >= limit:
                        raise LimitReached()

                async for v in _handle(href, depth):
                    yield v

        try:
            async for v in _handle(url, options.get('depth')):
                yield v

        except (LimitReached, DepthReached) as e:
            LOGGER.info(e.args[0])

    async def crawl(self, url, options=None):
        channel = self.ChannelModel(

        )

        return channel, self._iter_videos(url, auth, options)
