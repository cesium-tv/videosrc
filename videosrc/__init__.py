import asyncio
import inspect

import videosrc.crawlers
from videosrc.crawlers.html import HTMLCrawler
from videosrc.utils import iter_sync
from videosrc.errors import AuthenticationError


def detect_crawler(url):
    crawlers = []

    for cls in videosrc.crawlers.__dict__.values():
        if not inspect.isclass(cls):
            continue
        if callable(getattr(cls, 'check_url', None)):
            if cls.check_url(url):
                crawlers.append(cls)

    # Set a default crawler if none match.
    if not crawlers:
        crawlers.append(HTMLCrawler)

    return crawlers


async def login(url, **kwargs):
    credentials = kwargs.pop('credentials', {})

    crawler_klass = detect_crawler(url)[0]
    crawler = crawler_klass(**kwargs)

    try:
        return await crawler.login(url, **credentials)

    except:
        raise AuthenticationError('Failure logging in')


async def crawl(url, **kwargs):
    credentials = kwargs.pop('credentials', None)

    crawler_klass = detect_crawler(url)[0]
    crawler = crawler_klass(**kwargs)

    if credentials:
        await crawler.login(url, **credentials)

    return await crawler.crawl(url)


def login_sync(*args, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(login(*args, **kwargs))


def crawl_sync(*args, **kwargs):
    loop = asyncio.get_event_loop()
    channel, videos = loop.run_until_complete(crawl(*args, **kwargs))
    return channel, iter_sync(videos, loop=loop)
