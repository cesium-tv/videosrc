from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from videosrc.crawlers.twitter import TwitterCrawler


class TwitterTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.crawler = TwitterCrawler()
        self.server.get(
            self.server.url(),
            headers={'Content-Type': 'text/html'},
            body=RSP0)
        iframe_url = self.server.url('/embed/v1m7kuc/')
        self.server.get(
            self.server.url('/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/'),
            headers={'Content-Type': 'text/html'},
            body=RSP1.replace('%%URL%%', iframe_url))
        self.server.get(iframe_url,
            headers={'Content-Type': 'text/html'},
            body=RSP2)

    def tearDown(self):
        self.server.stop()

    async def test_crawl(self):
        self.crawler.crawl()
