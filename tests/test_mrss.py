from unittest import IsolatedAsyncioTestCase
from os.path import join as pathjoin, dirname, basename

from responses_server import ResponsesServer

from videosrc.crawlers.mrss import MRSSCrawler


BASE_PATH = dirname(dirname(__file__))

PATHS = ('/ForBiggerBlazes.mp4', '/ForBiggerEscapes.mp4')

MRSS = '''
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
   <channel>
      <title>Calm Meditation</title>
      <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com</link>
      <language>en-us</language>
      <pubDate>Mon, 02 Apr 2018 16:19:56 -0700</pubDate>
      <lastBuildDate>Mon, 02 Apr 2018 16:19:56 -0700</lastBuildDate>
      <managingEditor>tomjoht@gmail.com (Tom Johnson)</managingEditor>
      <description>Contains short videos capturing still scenes from nature with a music background, intended for calming or meditation purposes. When you're stressed out or upset, watch a few videos. As your mind focuses on the small details, let your worries and frustrations float away. The purpose is not to entertain or to distract, but to help calm, soothe, and surface your inner quiet. The videos contain scenes from the San Tomas Aquinas trail in Santa Clara, California.</description>
      <image>
         <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com</link>
         <title>Calm Meditation</title>
         <url>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/images/calmmeditationlogo_small.png</url>
         <description>Contains short videos capturing still scenes from nature with a music background, intended for calming or meditation purposes. When you're stressed out or upset, watch a few videos. As your mind focuses on the small details, let your worries and frustrations float away. The purpose is not to entertain or to distract, but to help calm, soothe, and surface your inner quiet. The videos contain scenes from the San Tomas Aquinas trail in Santa Clara, California.</description>
         <height>114</height>
         <width>114</width>
      </image>
      <atom:link href="http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/feed.xml" rel="self" type="application/rss+xml" />
      <item>
         <title>Shade</title>
         <pubDate>Mon, 23 Oct 2017 00:00:00 -0700</pubDate>
         <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/shade/</link>
         <description>Quiet the mind, and the soul will speak. - Ma Jaya Sati Bhagavati</description>
         <guid isPermaLink="false">http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/shade/</guid>
         <media:category>All</media:category>
         <media:category>Trail</media:category>
         <media:content url="%s" language="en-us" fileSize="37000000" duration="120.0" medium="video" isDefault="true">
            <media:title type="plain">Shade</media:title>
            <media:description type="html">Quiet the mind, and the soul will speak. - Ma Jaya Sati Bhagavati</media:description>
            <media:thumbnail url="http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/images/thumbs/shade.jpg" />
            <media:credit role="author" scheme="urn:ebu">Tom Johnson</media:credit>
            <media:copyright url="https://creativecommons.org/licenses/by/4.0/" />
         </media:content>
      </item>
      <item>
         <title>Spectators</title>
         <pubDate>Thu, 12 Oct 2017 00:00:00 -0700</pubDate>
         <link>http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/spectators/</link>
         <description>"Your worst enemy cannot harm you as much as your own thoughts, unguarded." – Buddha</description>
         <guid isPermaLink="false">http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/spectators/</guid>
         <media:category>All</media:category>
         <media:category>Grass</media:category>
         <media:content url="%s" language="en-us" fileSize="19000000" duration="120.0" medium="video" isDefault="true">
            <media:title type="plain">Spectators</media:title>
            <media:description type="html">"Your worst enemy cannot harm you as much as your own thoughts, unguarded." – Buddha</media:description>
            <media:thumbnail url="http://sample-firetv-web-app.s3-website-us-west-2.amazonaws.com/images/thumbs/spectators.jpg" />
            <media:credit role="author" scheme="urn:ebu">Tom Johnson</media:credit>
            <media:copyright url="https://creativecommons.org/licenses/by/4.0/" />
         </media:content>
      </item>
   </channel>
</rss>
'''


class MRSSTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.crawler = MRSSCrawler()
        self.server = ResponsesServer()
        self.server.start()
        self.files = []
        for path in PATHS:
            f = open(pathjoin(BASE_PATH, 'videos', basename(path)), 'rb')
            self.files.append(f)
            self.server.get(self.server.url(path), status=200, body=f)
        mrss = MRSS % (
            self.server.url(PATHS[0]),
            self.server.url(PATHS[1])
        )
        self.server.get(
            self.server.url(),
            status=200,
            body=mrss,
            headers={
                'Last-Modified': 'Sat, 15 Oct 2022 03:38:46 GMT',
                'Content-Length': str(len(mrss))}
            )

    def tearDown(self):
        self.server.stop()
        for f in self.files:
            f.close()

    async def test_login(self):
        await self.crawler.login('foobar', 'quux')
        self.assertEqual({
            'headers': {'Authorization': b'Zm9vYmFyOnF1dXg='}
        }, self.crawler.auth)

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl(self.server.url('/'))
        videos = [v async for v, s in videos]
        self.assertEqual('Calm Meditation', channel.name)
        self.assertEqual(2, len(videos))
        self.assertEqual('Shade', videos[0].title)
        self.assertEqual(
            'Quiet the mind, and the soul will speak. - Ma Jaya Sati Bhagavati',
            videos[0].description)
        self.assertListEqual(['All', 'Trail'], videos[0].tags)
        self.assertEqual(1, len(videos[0].sources))
        self.assertEqual(
            f'http://127.0.0.1:{self.server.port}/ForBiggerBlazes.mp4',
            videos[0].sources[0].url)
