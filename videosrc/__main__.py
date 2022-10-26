import asyncio
import logging

from pprint import pprint
from optparse import OptionParser

from videosrc import crawl


LOGGER = logging.getLogger('vidsrc')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler())


async def main(options, args):
    url, credentials = args[0], {}

    if options.username:
        credentials['username'] = options.username
        
    if options.password:
        credentials['password'] = options.password

    channel, videos = await crawl(url, credentials)

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
