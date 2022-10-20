import asyncio
import logging

from pprint import pprint
from optparse import OptionParser

from vidsrc import detect_crawler


LOGGER = logging.getLogger('vidsrc')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler())


async def main(options, args):
    url = args[0]
    crawler = detect_crawler(url)[0]()

    if options.username and options.password:
        await crawler.login(url, options.username, options.password)

    channel, videos = await crawler.crawl(url)
    pprint(channel)
    async for video, state in videos:
        pprint(video)


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option(
        '-u', '--username', help='Username')
    parser.add_option(
        '-p', '--password', help='Password')

    options, args = parser.parse_args()
    asyncio.run(main(options, args))
