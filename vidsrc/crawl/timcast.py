import re
import json
import asyncio
import logging
from urllib.parse import urljoin

import pyppeteer
from pyppeteer.errors import PyppeteerError
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from vidsrc.auth.timcast import TimcastAuth
from vidsrc.models import Video, VideoSource


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

RUMBLE_DOMAIN = re.compile(r'^https://rumble.com/embed/')
JSON_EXTRACT = re.compile(r'g\.f\["\w{6,7}"\]=({.*}),loaded:d\(\)')
JSON_TRIM = re.compile(r'^(.*)"path":.*,("w":.*$)')


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


async def _download(url, auth, options):
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
            r = await session.get_html(url, **auth)
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
                r = await session.get_html(src, **auth)
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


class TimcastCrawler:
    def __init__(self, url, options, state=None,
                 VideoModel=Video, VideoSourceModel=VideoSource):
        self.url = url
        self.options = options
        self.seen = set()
        if state is not None:
            self.state = state
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

    def crawl(self, url):
        auth = TimcastAuth(self.url).login(options.credentials)

        # NOTE: This code converts from async generator to sync generator.
        loop = asyncio.get_event_loop()
        ait = _download(url, auth, options).__aiter__()

        async def get_next():
            try:
                obj = await ait.__anext__()
                return False, obj

            except StopAsyncIteration:
                return True, None

        while True:
            done, obj = loop.run_until_complete(get_next())
            if done:
                break

            yield obj, self.state
