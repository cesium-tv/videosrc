import threading

from os.path import dirname, join as pathjoin
from unittest import TestCase, IsolatedAsyncioTestCase
from http.server import (
    HTTPServer as BaseHTTPServer,
    SimpleHTTPRequestHandler as BaseSimpleHTTPRequestHandler
)

from videosrc.crawlers.html import HTMLCrawler, url2title


VIDEOS_DIR = pathjoin(dirname(dirname(__file__)), 'videos')


class SimpleHTTPRequestHandler(BaseSimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, directory=VIDEOS_DIR)

    def log_message(self, format, *args):
        pass


class HTTPServer(BaseHTTPServer):
    def handle_error(self, *args, **kwargs):
        pass


class TestServer:
    def __init__(self):
        self._thread = None
        self._server = None

    @property
    def port(self):
        return self._server and self._server.server_address[1] or 0

    def url(self):
        return f'http://127.0.0.1:{self.port}/'

    def _run(self):
        self._server.serve_forever()

    def start(self):
        self._server = HTTPServer(('127.0.0.1', 0), SimpleHTTPRequestHandler)
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def stop(self):
        self._server.shutdown()
        self._thread.join()
        self._server.server_close()


class URL2TitleTestCase(TestCase):
    def test_url2title(self):
        for url, title in [
            ('trailing__spaces  ', 'Trailing Spaces'),
            ('camelCase', 'Camel Case'),
            ('TitleCase', 'Title Case'),
            ('no case', 'No Case'),
            ('  leading-spaces', 'Leading Spaces'),
            ('   lotsa    spaces    ', 'Lotsa Spaces')
        ]:
            with self.subTest(title=title):
                self.assertEqual(title, url2title(url))


class HTMLTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.crawler = HTMLCrawler()
        self.server = TestServer()
        self.server.start()

    def tearDown(self):
        self.server.stop()

    async def test_login(self):
        await self.crawler.login('foobar', 'quux')
        self.assertEqual({
            'headers': {'Authorization': b'Zm9vYmFyOnF1dXg='}
        }, self.crawler.auth)

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl(self.server.url())
        videos = [v async for v, s in videos]
        self.assertEqual('Directory listing for /', channel.name)
        self.assertEqual(5, len(videos))
        self.assertIsNotNone(videos[0].extern_id)
        self.assertEqual('For Bigger Blazes', videos[0].title)
        self.assertEqual(719760, videos[0].duration)
        self.assertEqual(1, len(videos[0].sources))
        self.assertEqual(1280, videos[0].sources[0].width)
        self.assertEqual(720, videos[0].sources[0].height)
