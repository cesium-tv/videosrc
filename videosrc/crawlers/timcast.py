import os
import re
import time
import asyncio
import logging

from urllib.parse import urljoin, urlparse

import pyppeteer
from pyppeteer.errors import PyppeteerError
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.utils import get_tag_text, md5sum
from videosrc.crawlers.rumble import (
    get_embed_details, parse_date, extract_sources,
)
from videosrc.crawlers.base import Crawler
from videosrc.errors import StateReached


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

PYPPETEER_WS_URL = os.getenv('PYPPETEER_WS_URL')

RUMBLE_DOMAIN = re.compile(r'^https://rumble.com/embed/')
JSON_EXTRACT = re.compile(r'g\.f\["\w{6,7}"\]=({.*}),loaded:d\(\)')
JSON_TRIM = re.compile(r'^(.*)"path":.*,("w":.*$)')
U_FIELD = '#user_login'
P_FIELD = '#user_pass'
SUBMIT = '#wp-submit'


def _no_images_or_css(request):
    if request.resourceType() in ('image', 'stylesheet', 'font'):
        request.abort_()
    else:
        request.continue_()


async def pyppeteer_browser(*args, **kwargs):
    headless = kwargs.pop('headless', False)

    if PYPPETEER_WS_URL:
        LOGGER.info('Using remote chrome instance')
        browser = await pyppeteer.connect(PYPPETEER_WS_URL, **kwargs)

    else:
        LOGGER.info('Lanching chrome instance')
        browser = await pyppeteer.launch(
            headless=headless,
            args=args,
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
            **kwargs,
        )

    return browser


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
        return urlparse(url).netloc.endswith('timcast.com')

    async def _login(self, url, username, password, headless=True,
                     login_timeout=12000):
        args = [
            '--start-maximized',
            # '--no-sandbox',
            '--disable-setuid-sandbox',
        ]
        if self._proxy:
            args.append(f'--proxy-server={self._proxy}')

        browser = await pyppeteer_browser(
            *args, headless=headless, ignoreHTTPSError=True)
        page = await browser.newPage()

        try:
            await page.setViewport({'width': 1366, 'height': 768})
            await page.setRequestInterception(True)
            page.on('request', _no_images_or_css)

            LOGGER.debug('Opening url: %s', url)
            await page.goto(url, timeout=login_timeout, waitFor='networkidle2')

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

    async def login(self, url, username, password, **kwargs):
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
                raise StateReached()

            sources = extract_sources(video_details, self.VideoSourceModel)
            if not sources:
                LOGGER.warning('Video has no sources! Skipping...')
                continue

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
                try:
                    async for video in self._iter_page_videos(url, page):
                        yield video
                except StateReached:
                    LOGGER.debug('Aborting, state reached', exc_info=True)
                    break
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
        try:
            username = kwargs.pop('username')
            password = kwargs.pop('password')

        except KeyError:
            LOGGER.warning('No credentials, skipping login')

        else:
            await self.login(url, username, password, **kwargs)

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
