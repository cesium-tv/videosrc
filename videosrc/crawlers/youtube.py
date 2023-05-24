import logging

from urllib.parse import urlparse

from videosrc.crawlers.base import Crawler


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class YoutubeCrawler(Crawler):
    @staticmethod
    def check_url(url):
        return urlparse(url).netloc.endswith('youtube.com')
