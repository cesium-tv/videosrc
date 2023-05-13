import logging
import json

from urllib.parse import urlparse

import snscrape.modules.twitter as sntwitter

from videosrc.crawlers.base import Crawler
from videosrc.utils import md5sum, MediaInfo


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class TwitterCrawler(Crawler):
    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('twitter.com')

    async def _iter_videos(self, url, items):
        for item in items:
            try:
                media = item.media[0]
            except (TypeError, IndexError):
                continue
            if not isinstance(media, sntwitter.Video):
                continue

            sources = []
            for variant in media.variants:
                #info = MediaInfo(variant.url)
                sources.append(self.VideoSourceModel(
                    extern_id=md5sum(variant.url),
                    width=0,   # info.frame.width,
                    height=0,  # info.frame.height,
                    #fps=info.stream.guessed_rate,
                    size=0,    # info.size,
                    url=variant.url,
                    original={
                        'url': variant.url,
                        # 'video': dict_repr(info.video),
                    },
                ))
            video = self.VideoModel(
                extern_id=item.id,
                title=item.rawContent,
                poster=media.thumbnailUrl,
                duration=media.duration,
                published=item.date,
                sources=sources,
                original={
                    'url': item.url,
                    'json': json.loads(item.json()),
                },
            )

            try:
                yield video
            except Exception as e:
                LOGGER.exception(e)

    # https://twitter.com/MattWalshShow
    async def crawl(self, url, **options):
        # Parse name from URL
        name = urlparse(url).path.strip('/')
        # Get the tweets:
        items = sntwitter.TwitterSearchScraper(f'from:{name}').get_items()
        channel = self.ChannelModel(
            extern_id=md5sum(name),
            name=name,
            url=url,
        )
        return channel, self._iter_videos(url, items)

