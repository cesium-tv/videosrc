import inspect

import vidsrc.crawl
from vidsrc.crawl.html import HTMLCrawler


def detect_crawler(url):
    crawlers = []

    for attr in dir(vidsrc.crawl):
        cls = getattr(vidsrc.crawl, attr)
        if not inspect.isclass(cls):
            continue
        if callable(getattr(cls, 'check_url', None)):
            if cls.check_url(url):
                crawlers.append(cls)

    # Set a default crawler if none match.
    if not crawlers:
        crawlers.append(HTMLCrawler)

    return crawlers