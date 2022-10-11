import asyncio
import logging
import time
from urllib.parse import urljoin

import pyppeteer
from pyppeteer.errors import PyppeteerError


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

U_FIELD = '#user_login'
P_FIELD = '#user_pass'
SUBMIT = '#wp-submit'


async def _login(url, credentials, headless=True, timeout=2000):
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
        return '; '.join(cookieStr)

    finally:
        await page.close()
        await browser.close()


class TimcastAuth:
    def __init__(self, url):
        self.url = url

    def login(self, credentials, headless=True, retry=3, timeout=2000):
        url = urljoin(self.url, '/login/')
        loop = asyncio.get_event_loop()

        for i in range(1, 1 + retry):
            try:
                LOGGER.debug('Login attempt %i', i + 1)
                return loop.run_until_complete(_login(
                    url, credentials, headless=headless, retry=retry,
                    timeout=timeout
                ))

            except (PyppeteerError, asyncio.TimeoutError):
                if i == retry:
                    raise

                LOGGER.exception('Login failed, retrying')
                time.sleep(3 ** i)
