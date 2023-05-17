import re
import types
import asyncio
import logging

from base64 import b64encode
from numbers import Number
from fractions import Fraction
from datetime import datetime
from email.utils import parsedate_to_datetime
from io import BytesIO
from urllib.parse import quote, urlparse
from os.path import splitext, basename
from hashlib import md5
from mimetypes import guess_type

import av
import requests


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


def md5sum(s):
    try:
        s = s.encode()
    except UnicodeEncodeError:
        pass
    return md5(s).hexdigest()


def get_tag_text(o, name):
    tag = o.find(name)
    return tag and tag.text


def basic_auth(username, password):
    auth = f'{username}:{password}'.encode()
    return {
        'headers': {
            'Authorization': b64encode(auth).decode(),
        },
    }


def isiterable(o):
    try:
        iter(o)
    except TypeError:
        return False
    else:
        return True


def dict_repr(o):
    d = {}
    for name in dir(o):
        if name.startswith('_'):
            continue
        value = getattr(o, name)
        if isinstance(value, Fraction):
            d[name] = float(value)
        elif isinstance(value, Number):
            d[name] = value
        elif isinstance(value, str):
            d[name] = value
        elif isinstance(value, types.FunctionType):
            continue
        elif isiterable(value):
            d[name] = [
                dict_repr(oo) for oo in value
            ]

    return d


def url2title(url):
    urlp = urlparse(url)
    fn = splitext(basename(urlp.path))[0]
    wupper = [
        s for s in [s.strip() for s in re.split(r'(?=[A-Z])', fn)] if s
    ]
    wnword = [
        s for s in [s.strip() for s in re.split(r'[\s\-_=+]+', fn)] if s
    ]
    words = wupper if len(wupper) > len(wnword) else wnword
    return ' '.join(words).title()


def url2mime(url):
    return guess_type(urlparse(url).path)[0]


def iter_sync(f, loop=None):
    # NOTE: This code converts from async generator to sync generator.
    loop = loop or asyncio.get_event_loop()
    ait = f.__aiter__()

    async def get_next():
        try:
            obj = await ait.__anext__()
            return False, obj

        except StopAsyncIteration:
            return True, None

    while True:
        done, obj = loop.run_until_complete(get_next())
        if done:
            break

        yield obj


async def aenumerate(seq, start=0):
    n = start
    async for e in seq:
        yield n, e
        n += 1


class MediaInfo:
    """
    Decodes remote video file.

    Uses lazy-loading properties to do as little work as is necessary.
    """
    def __init__(self, url):
        self.url = url
        self._video = None
        self._frame = None
        self._headers = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @property
    def headers(self):
        if self._headers is None:
            # NOTE: We have not yet fetched headers, do a quick HEAD request.
            with requests.head(self.url) as r:
                self._headers = r.headers
        return self._headers

    @property
    def video(self):
        if self._video is None:
            with requests.get(self.url, stream=True) as r:
                self._headers = r.headers
                try:
                    self._video = av.open(r.raw)
                except Exception as e:
                    LOGGER.warning(e, exc_info=True)
        return self._video

    @property
    def stream(self):
        try:
            return self.video.streams.video[0]
        except IndexError as e:
            LOGGER.warning(e, exc_info=True)
            return None

    @property
    def frame(self):
        if self._frame is None:
            stream = self.stream
            stream.codec_context.skip_frame = "NONKEY"
            self._frame = next(self.video.decode(stream))
        return self._frame

    @property
    def size(self):
        return int(self.headers.get('Content-Length', 0))

    @property
    def mime(self):
        return self.headers.get('Content-Type')

    @property
    def width(self):
        try:
            return self.stream.width
        except AttributeError:
            return None

    @property
    def height(self):
        try:
            return self.stream.height
        except AttributeError:
            return None

    @property
    def duration(self):
        try:
            return self.stream.duration
        except AttributeError:
            return None

    @property
    def fps(self):
        try:
            return self.stream.guessed_rate
        except AttributeError:
            return None

    def last_modified(self, default=datetime.now):
        try:
            last_modified = self.headers['Last-Modified']
        except KeyError:
            return default() if callable(default) else default
        return parsedate_to_datetime(last_modified)

    def poster(self):
        poster = BytesIO()
        self.frame.to_image().save(poster, format='png')
        return f'data:image/png;base64,{quote(b64encode(poster.getvalue()))}'

    def close(self):
        if self._video is not None:
            self._video.close()
