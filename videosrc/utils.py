import re
import types
import asyncio

from base64 import b64encode
from numbers import Number
from fractions import Fraction
from datetime import datetime
from email.utils import parsedate_to_datetime
from io import BytesIO
from urllib.parse import urljoin, quote, urlparse
from base64 import b64encode
from os.path import splitext, basename

import av
import requests
from bs4 import BeautifulSoup


def get_tag_text(o, name):
    tag = o.find(name)
    return tag and tag.text


def basic_auth(username, password):
    return {
        'headers': {
            'Authorization': b64encode(f'{username}:{password}'.encode()).decode(),
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
        s for s in [s.strip() for s in re.split('(?=[A-Z])', fn)] if s
    ]
    wnword = [
        s for s in [s.strip() for s in re.split('[\s\-_=+]+', fn)] if s
    ]
    words = wupper if len(wupper) > len(wnword) else wnword
    return ' '.join(words).title()


def iter_sync(f):
    # NOTE: This code converts from async generator to sync generator.
    loop = asyncio.get_event_loop()
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
                self._video = av.open(r.raw)
        return self._video

    @property
    def stream(self):
        return self.video.streams.video[0]

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

    def last_modified(self, default=datetime.now):
        try:
            last_modified = self.headers['Last-Modified']
        except KeyError:
            return default() if callable(default) else default
        parsedate_to_datetime(last_modified)

    def poster(self):
        poster = BytesIO()
        self.frame.to_image().save(poster, format='png')
        return f'data:image/png;base64,{quote(b64encode(poster.getvalue()))}'

    def close(self):
        if self._video is not None:
            self._video.close()
