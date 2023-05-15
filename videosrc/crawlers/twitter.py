import logging
import json

from urllib.parse import urlparse

from snscrape.modules import twitter as sntwitter
from snscrape.base import ScraperException

from videosrc.crawlers.base import Crawler
from videosrc.utils import md5sum, MediaInfo, dict_repr
from videosrc.errors import InvalidOptionError


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class TwitterCrawler(Crawler):
    def __init__(self, state=0, **kwargs):
        super().__init__(state=state, **kwargs)

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('twitter.com')

    async def _iter_videos(self, url, items, max_count=100, max_days=None):
        for item in items:
            try:
                media = item.media[0]
            except (TypeError, IndexError):
                continue
            if not isinstance(media, sntwitter.Video):
                continue

            sources = []
            for variant in media.variants:
                with MediaInfo(variant.url) as info:
                    sources.append(self.VideoSourceModel(
                        extern_id=md5sum(variant.url),
                        width=info.width,
                        height=info.height,
                        fps=info.fps,
                        size=info.size,
                        mime=variant.contentType,
                        url=variant.url,
                        original={
                            'url': variant.url,
                            'variant': dict_repr(variant),
                            'video': dict_repr(info.video),
                        },
                    ))

            video = self.VideoModel(
                extern_id=item.id,
                title=item.rawContent,
                poster=media.thumbnailUrl,
                duration=media.duration,
                published=item.date,
                sources=sources,
                tags=item.hashtags,
                original={
                    'url': item.url,
                    'json': json.loads(item.json()),
                },
            )

            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

            else:
                self._state = max(item.id, self._state)

    # https://twitter.com/MattWalshShow
    async def crawl(self, url, **kwargs):
        # Parse name from URL
        name = urlparse(url).path.strip('/')
        proxies = {}
        if self._proxy:
            proxies['http'] = self._proxy
            proxies['https'] = self._proxy

        # Get the tweets:
        try:
            items = sntwitter.TwitterUserScraper(
                name,
                proxies=proxies,
            ).get_items()

        except ScraperException as e:
            LOGGER.error(e.args[0])
            raise InvalidOptionError('Unknown twitter user %s' % name)

        channel = self.ChannelModel(
            extern_id=md5sum(name),
            name=name,
            url=url,
        )
        return channel, self.iter_videos(url, items, **kwargs)
