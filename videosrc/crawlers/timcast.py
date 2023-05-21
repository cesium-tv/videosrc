import re
import time
import asyncio
import logging

from urllib.parse import urljoin, urlparse

import pyppeteer
from pyppeteer.errors import PyppeteerError
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.utils import get_tag_text, md5sum, url2mime
from videosrc.crawlers.rumble import get_embed_details, parse_date
from videosrc.crawlers.base import Crawler


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


class TimcastCrawler(Crawler):
    auth_fields = {
        'username': 'String',
        'password': 'String',
    }

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.auth = {}

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('timcast.com')

    async def _login(self, url, username, password, headless=True,
                     timeout=2000):
        args = [
            '--start-maximized',
            '--no-sandbox',
            '--disable-setuid-sandbox',
        ]
        if self._proxy:
            args.append(f'--proxy-server={self._proxy}')
        browser = await pyppeteer.launch(
            headless=headless,
            args=args,
            ignoreHTTPSError=True,
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False
        )

        page = await browser.newPage()

        try:
            await page.setViewport({'width': 1366, 'height': 768})

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

    async def login(self, url, **kwargs):
        try:
            username = kwargs['username']
            password = kwargs['password']
        except KeyError:
            LOGGER.warning('No credentials, skipping login')
            return

        retry = kwargs.pop('retry', 3)
        url = urljoin(url, '/login/')

        for i in range(1, 1 + retry):
            try:
                LOGGER.debug('Login attempt %i', i)
                self.auth = await self._login(
                    url, username, password, **kwargs)
                break

            except (PyppeteerError, asyncio.TimeoutError):
                if i == retry:
                    raise

                LOGGER.exception('Login failed, retrying')
                time.sleep(3 ** i)

    async def _iter_page_videos(self, url, page):
        grid = page.find(
            'div', class_='t-grid:s:fit:2 t-grid:m:fit:4 t-pad:25pc:top')
        state = self._state
        for article in grid.find_all('div', class_='article'):
            video_link = article.find('a', class_='image')
            thumbnail = video_link.img['src']
            description = video_link.img['alt']
            video_page_url = video_link['href']
            video_page_url = urljoin(url, urlparse(video_page_url).path)
            async with ScraperSession() as s:
                video_page = BeautifulSoup(
                    await s.get_html(video_page_url, proxy=self._proxy,
                                     **self.auth),
                    'html.parser')
            try:
                iframe_tag = video_page.find('iframe')
                embed_url = iframe_tag['src']

            except TypeError:
                LOGGER.warning('Skipped video, missing iframe', exc_info=True)
                continue

            video_details = await get_embed_details(
                embed_url, proxy=self._proxy)
            pubDate = parse_date(video_details['pubDate'])

            if state and pubDate < state:
                LOGGER.info('Video published before last state %s', pubDate)
                return

            sources = [
                self.VideoSourceModel(
                    extern_id=md5sum(src['url']),
                    width=src['meta']['w'],
                    height=src['meta']['h'],
                    size=src['meta']['size'],
                    mime=url2mime(src['url']),
                    url=src['url'],
                    original=src,
                ) for src in video_details['ua']['mp4'].values()
            ]
            video = self.VideoModel(
                extern_id=md5sum(video_page_url),
                title=description,
                poster=thumbnail,
                duration=video_details['duration'],
                published=pubDate,
                original=str(article),
                sources=sources,
            )

            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

            else:
                self._state = max(self._state, pubDate) if self._state \
                                                        else pubDate

    async def _iter_videos(self, url, page):
        page_num = 1
        async with ScraperSession() as s:
            while True:
                LOGGER.debug('Scraping page %i', page_num)
                async for video in self._iter_page_videos(url, page):
                    yield video
                page_num += 1
                page_url = url + f'page/{page_num}/'
                urlp = urlparse(page_url)
                if not page.find('a', href=urlp.path[:-1]):
                    LOGGER.debug('No more pages')
                    break
                html = await s.get_html(
                    page_url, proxy=self._proxy, **self.auth)
                page = BeautifulSoup(html, 'html.parser')

    async def crawl(self, url, **kwargs):
        await self.login(url, **kwargs)

        async with ScraperSession() as s:
            page = BeautifulSoup(
                await s.get_html(
                    url, proxy=self._proxy, **self.auth), 'html.parser')
            title = get_tag_text(page, 'h1')
            channel = self.ChannelModel(
                extern_id=md5sum(url),
                url=url,
                name=title,
            )

        return channel, self.iter_videos(url, page, **kwargs)
