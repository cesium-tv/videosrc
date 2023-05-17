import logging
import pickle

from urllib.parse import urlparse
from pprint import pprint
from argparse import ArgumentParser, ArgumentTypeError

from videosrc import crawl_sync


LOGGER = logging.getLogger('vidsrc')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler())


def url(s):
    urlp = urlparse(s)
    if all((urlp.scheme, urlp.netloc)):
        return s
    raise ArgumentTypeError('Invalid URL')


def save_state_factory(path):
    def _save_state(state):
        LOGGER.info('Saving state to file %s', path)
        with open(path) as f:
            pickle.dump(f, state)
    return _save_state


def load_state(path):
    LOGGER.info('Loading state from file %s', path)
    with open(path, 'rb') as f:
        return pickle.load(f)


def main(args):
    credentials = {}
    kwargs = {'credentials': credentials}
    url = args.url

    if args.username:
        credentials['username'] = args.username

    if args.password:
        credentials['password'] = args.password

    if args.state:
        kwargs['state'] = load_state(args.state)
        kwargs['save_state'] = save_state_factory(args.state)

    if args.proxy:
        kwargs['proxy'] = args.proxy

    channel, videos = crawl_sync(url, **kwargs)

    pprint(channel)
    for video in videos:
        pprint(video)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('url', type=url, help='URL to collect video from')
    parser.add_argument(
        '-u', '--username', help='Username')
    parser.add_argument(
        '-p', '--password', help='Password')
    parser.add_argument(
        '-P', '--proxy', type=url, help='Proxy server url')
    parser.add_argument(
        '-s', '--state', help='Path at which to save crawl state')

    args = parser.parse_args()
    main(args)
