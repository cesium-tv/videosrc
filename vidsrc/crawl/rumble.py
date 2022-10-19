import re
import json

from os.path import split as pathsplit
from urllib.parse import urlparse, urljoin
from hashlib import md5
from datetime import datetime
from pprint import pprint

from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from vidsrc.auth.rumble import RumbleAuth
from vidsrc.models import Channel, Video, VideoSource
from vidsrc.utils import sync_iter


JSON_EXTRACT = re.compile(r'\w\.\w\["\w{6,7}"\]=({.*}),loaded:\w\(\)')


async def get_video_details(url):
    async with ScraperSession() as s:
        video_page = BeautifulSoup(await s.get_html(url), 'html.parser')
        script_tag = video_page.find('script', type='application/ld+json')
        video_details = json.loads(script_tag.text)
        embed_url = video_details[0]['embedUrl']
        urlp = urlparse(embed_url)
        embed_url = urljoin(url, urlp.path)
        embed_page = await s.get_html(embed_url)
        m = JSON_EXTRACT.search(embed_page)
        return json.loads(f'{m.group(1)}}}')


def parse_date(s):
    # 2022-10-18T13:02:12+00:00
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S%z')


class RumbleCrawler:
    def __init__(self, state=None, ChannelModel=Channel,
                 VideoModel=Video, VideoSourceModel=VideoSource):
        self.state = state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('rumble.com')

    async def _crawl_videos(self, url, page):
        for li in page.find_all('li', class_='video-listing-entry'):
            url = urljoin(url, li.article.a['href'])
            video_details = await get_video_details(url)
            sources = [
                self.VideoSourceModel(
                    width=src['meta']['w'],
                    height=src['meta']['h'],
                    size=src['meta']['size'],
                    url=src['url'],
                    original=src,
                ) for src in video_details['ua']['mp4'].values()
            ]
            video = self.VideoModel(
                extern_id=md5(url.encode()).hexdigest(),
                title=li.article.h3.text,
                poster=li.article.img['src'],
                duration=video_details['duration'],
                published=parse_date(video_details['pubDate']),
                sources=sources,
                original=str(li),
            )
            yield str(video)

    async def crawl(self, url):
        # https://rumble.com/user/vivafrei
        urlp = urlparse(url)
        pparts = pathsplit(urlp.path)

        async with ScraperSession() as s:
            page = BeautifulSoup(await s.get_html(url), 'html.parser')

        thumb = page.find('img', class_='listing-header--thumb')
        poster = thumb.src if thumb else None
        channel = self.ChannelModel(
            title=pparts[-1],
            name=pparts[-1],
            url=url,
            poster=poster,
        )

        return channel, self._crawl_videos(url, page)
