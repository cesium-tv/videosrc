from unittest import IsolatedAsyncioTestCase

from responses_server import ResponsesServer

from vidsrc.crawl.timcast import TimcastCrawler


class TimcastTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer()
        self.server.start()
        self.crawler = TimcastCrawler()

    def tearDown(self):
        self.server.stop()

    async def test_login(self):
        pass

    async def test_crawl(self):
        pass
