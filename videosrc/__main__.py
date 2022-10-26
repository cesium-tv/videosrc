import asyncio
import logging

from pprint import pprint
from optparse import OptionParser

from videosrc import crawl_sync


LOGGER = logging.getLogger('vidsrc')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler())


def main(options, args):
    url, credentials = args[0], {}

    if options.username:
        credentials['username'] = options.username
        
    if options.password:
        credentials['password'] = options.password

    channel, videos = crawl_sync(url, credentials=credentials)

    pprint(channel)
    for video, state in videos:
        pprint(video)


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option(
        '-u', '--username', help='Username')
    parser.add_option(
        '-p', '--password', help='Password')

    options, args = parser.parse_args()
    main(options, args)
