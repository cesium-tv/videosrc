import logging

from urllib.parse import urlparse

from pytube import Channel
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.crawlers.base import Crawler
from videosrc.utils import md5sum, get_tag_text


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class YoutubeCrawler(Crawler):
    @staticmethod
    def check_url(url):
        return urlparse(url).netloc.endswith('youtube.com')

    async def _iter_videos(self, url, c, **kwargs):
        for v in c.videos:
            sources = []
            for s in v.streams:
                res = int(s.res[:-1])
                fps = int(s.fps[:-3])
                sources.append(self.VideoSourceModel(
                    extern_id=md5sum(s.url),
                    url=s.url,
                    mime=s.mime_type,
                    width=res,
                    fps=fps,
                    size=s.filesize,
                ))

            video = self.VideoModel(
                extern_id=v.video_id,
                sources=sources,
                duration=v.length,
                title=v.title,
                published=v.publish_date,
                original=v.metadata,
                tags=v.keywords,
                poster=v.thumbnail_url,
            )

            yield video

    # https://www.youtube.com/c/ProgrammingKnowledge
    async def crawl(self, url, **kwargs):
        c = Channel(url, proxies={'http': self._proxy, 'https': self._proxy})

        async with ScraperSession() as s:
            html = await s.get_html(c.about_url, proxy=self._proxy)
            page = BeautifulSoup(html, 'html.parser')

        channel_name = get_tag_text(
            page, 'yt-formatted-string', class_='style-scope ytd-channel-name')
        poster_tag = page.find('img', id='img')
        poster = poster_tag.src if poster_tag else None
        desc = get_tag_text(page, 'yt-formatted-string', id='description')

        channel = self.ChannelModel(
            extern_id=c.playlist_id,
            name=channel_name,
            url=c.channel_url,
            title=channel_name,
            description=desc,
            poster=poster,
            original=c.initial_data,
        )

        return channel, self.iter_videos(url, c, **kwargs)
