import re
import time
import json
import asyncio
import logging

from urllib.parse import urljoin, urlparse
from hashlib import md5
from datetime import datetime
from pprint import pprint

import pyppeteer
from pyppeteer.errors import PyppeteerError
from aiohttp.hdrs import METH_HEAD
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.models import Channel, Video, VideoSource
from videosrc.utils import get_tag_text
from videosrc.crawlers.rumble import get_embed_details, parse_date


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
        self.state = state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('timcast.com')

    async def _login(self, url, username, password, headless=True, timeout=2000):
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

            LOGGER.debug('Opening url: %s', url)
            await page.goto(url, timeout=timeout, waitFor='networkidle2')

            LOGGER.debug('Typing')
            await page.type(U_FIELD, username)
            await page.type(P_FIELD, password)

            LOGGER.debug('Clicking submit')
            await page.click(SUBMIT)

            cookieStr = []
            for cookie in await page.cookies():
                cookieStr.append(f"{cookie['name']}={cookie['value']}")
            return {'headers': {'Cookies': '; '.join(cookieStr)}}

        finally:
            await page.close()
            await browser.close()

    async def login(self, url, username, password, headless=True, retry=3, timeout=2000):
        url = urljoin(url, '/login/')

        for i in range(1, 1 + retry):
            try:
                LOGGER.debug('Login attempt %i', i)
                self.auth = await self._login(
                    url, username, password, headless=headless, timeout=timeout
                )
                break

            except (PyppeteerError, asyncio.TimeoutError):
                if i == retry:
                    raise

                LOGGER.exception('Login failed, retrying')
                time.sleep(3 ** i)

    async def _iter_videos(self, url, page):
        grid = page.find('div', class_='t-grid:s:fit:2 t-grid:m:fit:4 t-pad:25pc:top')
        for article in grid.find_all('div', class_='article'):
            date = article.find('div', class_='summary').div.text
            (m, d, y) = map(int, date.split('.'))
            state = datetime(y + 2000, m, d)
            if self.state and self.state > state:
                LOGGER.info('Video published before given state')
                break

            video_link = article.find('a', class_='image')
            thumbnail = video_link.img['src']
            description = video_link.img['alt']
            video_page_url = video_link['href']
            video_page_url = urljoin(url, urlparse(video_page_url).path)
            async with ScraperSession() as s:
                video_page = BeautifulSoup(
                    await s.get_html(video_page_url, **self.auth),
                    'html.parser')
            iframe_tag = video_page.find('iframe')
            embed_url = iframe_tag['src']
            video_details = await get_embed_details(embed_url)
            sources = [
                self.VideoSourceModel(
                    width=src['meta']['w'],
                    height=src['meta']['h'],
                    size=src['meta']['size'],
                    url=src['url'],
                    original=src,
                ) for src in video_details['ua']['mp4'].values()
            ]
            yield self.VideoModel(
                extern_id=md5(video_page_url.encode()).hexdigest(),
                title=description,
                poster=thumbnail,
                duration=video_details['duration'],
                published=parse_date(video_details['pubDate']),
                original=str(article),
                sources=sources,
            ), state

    async def _iter_pages(self, url, page):
        page_num = 1
        async with ScraperSession() as s:
            while True:
                LOGGER.debug('Scraping page %i', page_num)
                async for video in self._iter_videos(url, page):
                    yield video
                page_num += 1
                page_url = url + f'page/{page_num}/'
                urlp = urlparse(page_url)
                if not page.find('a', href=urlp.path[:-1]):
                    LOGGER.debug('No more pages')
                    break
                page = BeautifulSoup(
                    await s.get_html(page_url, **self.auth), 'html.parser')

    async def crawl(self, url, options=None):
        async with ScraperSession() as s:
            page = BeautifulSoup(
                await s.get_html(url, **self.auth), 'html.parser')
            title = get_tag_text(page, 'h1')
            channel = self.ChannelModel(
                url=url,
                name=title,
            )

        return channel, self._iter_pages(url, page)
