import asyncio

from pprint import pprint
from optparse import OptionParser

from vidsrc import detect_crawler


async def main(options, args):
    url = args[0]

    crawler = detect_crawler(url)[0]()
    channel, videos = await crawler.crawl(url)
    pprint(channel)
    async for video in videos:
        pprint(video)


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option(
        '-c', '--crawler', help='Choose crawler implementation')
    options, args = parser.parse_args()

    asyncio.run(main(options, args))
