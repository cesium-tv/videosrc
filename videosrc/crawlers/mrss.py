import logging

from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

from aiohttp.hdrs import METH_GET
from aiohttp_scraper import ScraperSession
from bs4 import BeautifulSoup

from videosrc.models import Video, VideoSource
from videosrc.utils import MediaInfo, get_tag_text, md5sum
from videosrc.crawlers.html import HTMLCrawler


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class MRSSCrawler(HTMLCrawler):
    auth_fields = {
        'username': 'String',
        'password': 'String',
    }

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.path.endswith('.mrss')

# <item>
#     <title>Shade</title>
#     <pubDate>Mon, 23 Oct 2017 00:00:00 -0700</pubDate>
#     <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/shade/</link>
#     <description>Quiet the mind, and the soul will speak. - Ma Jaya Sati
#       Bhagavati</description>
#     <guid isPermaLink="false">
#       http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/shade/
#     </guid>
#     <media:category>All</media:category>
#     <media:category>Trail</media:category>
#     <media:content url="http://d1nixf144dcz0j.cloudfront.net/shade.mp4"
#       language="en-us" fileSize="37000000" duration="120.0" medium="video"
#       isDefault="true">
#     <media:title type="plain">Shade</media:title>
#     <media:description type="html">Quiet the mind, and the soul will speak.
#       - Ma Jaya Sati Bhagavati</media:description>
#     <media:thumbnail
#       url="http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com
#            /images/thumbs/shade.jpg"
#     />
#     <media:credit role="author" scheme="urn:ebu">Tom Johnson</media:credit>
#     <media:copyright url="https://creativecommons.org/licenses/by/4.0/" />
#     </media:content>
# </item>
    async def _iter_videos(self, soup):
        for item in soup.find_all('item'):
            content = item.find('media:content')
            url = content['url']
            guid = item.guid.text or md5sum(url)
            title = get_tag_text(item, 'media:title') or \
                get_tag_text(item, 'title')
            description = get_tag_text(item, 'media:description') or \
                get_tag_text(item, 'description')
            poster = get_tag_text(item, 'media:thumbnail')
            published = parsedate_to_datetime(item.pubDate.text)
            keywords = get_tag_text(item, 'media:keywords')
            if keywords:
                keywords = [s.strip() for s in keywords.split(',')]
            else:
                keywords = []
            keywords.extend([
                t.text for t in item.find_all('media:category')
            ])
            with MediaInfo(url) as info:
                source = VideoSource(
                    extern_id=guid,
                    width=info.width,
                    height=info.height,
                    fps=info.fps,
                    size=int(content.get('fileSize', info.size)),
                    url=url,
                    mime=info.mime,
                    original={},
                )
                video = Video(
                    extern_id=guid,
                    title=title,
                    description=description,
                    poster=poster,
                    duration=float(content.get('duration', info.duration)),
                    published=published,
                    tags=keywords,
                    sources=[source],
                    original={
                        'url': url,
                        'headers': dict(info.headers),
                        'tag': str(item),
                    },
                )

            try:
                yield video

            except Exception as e:
                LOGGER.exception(e)

# <channel>
#     <title>Calm Meditation</title>
#     <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com</link>
#     <language>en-us</language>
#     <pubDate>Mon, 02 Apr 2018 16:19:56 -0700</pubDate>
#     <lastBuildDate>Mon, 02 Apr 2018 16:19:56 -0700</lastBuildDate>
#     <managingEditor>tomjoht@gmail.com (Tom Johnson)</managingEditor>
#     <description>Contains short videos capturing still scenes from nature
#       with a music background, intended for calming or meditation purposes.
#       When you're stressed out or upset, watch a few videos. As your mind
#       focuses on the small details, let your worries and frustrations float
#       away. The purpose is not to entertain or to distract, but to help
#       calm, soothe, and surface your inner quiet. The videos contain scenes
#       from the San Tomas Aquinas trail in Santa Clara, California.
#     </description>
#     <image>
#         <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com</link>
#         <title>Calm Meditation</title>
#         <url>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/images/calmmeditationlogo_small.png</url>
#         <description>Contains short videos capturing still scenes from
#           nature with a music background, intended for calming or
#           meditation purposes. When you're stressed out or upset, watch a
#           few videos. As your mind focuses on the small details, let your
#           worries and frustrations float away. The purpose is not to
#           entertain or to distract, but to help calm, soothe, and surface
#           your inner quiet. The videos contain scenes from the San Tomas
#           Aquinas trail in Santa Clara, California.</description>
#         <height>114</height>
#         <width>114</width>
#     </image>
    async def crawl(self, url, **kwargs):
        await self.login(url, **kwargs)

        async with ScraperSession() as s:
            r = await s._request(METH_GET, url, proxy=self._proxy)
            try:
                state = {
                    'Last-Modified': parsedate_to_datetime(
                        r.headers['Last-Modified']),
                    'Content-Length': int(r.headers['Content-Length']),
                }
            except KeyError as e:
                LOGGER.warning(
                    'Could not read header: %s, unknown state', e.args[0])

            else:
                if self._state == state:
                    LOGGER.info('Matching state, no updates')
                    return
                else:
                    self._state = state

            soup = BeautifulSoup(await r.text(), 'xml')
            tag = soup.find('channel')
            channel = self.ChannelModel(
                extern_id=md5sum(url),
                name=tag.title.text,
                url=url,
                description=tag.description.text,
                poster=tag.image.url.text,
            )
            return channel, self._iter_videos(soup)
