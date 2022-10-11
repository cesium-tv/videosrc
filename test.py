import os
import re
import logging
from pprint import pprint

from vidsrc import download


TIMCAST_USERNAME = os.getenv('TIMCAST_USERNAME')
TIMCAST_PASSWORD = os.getenv('TIMCAST_PASSWORD')

LOGGER = logging.getLogger('vidsrc')
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.DEBUG)

options = {
    'headless': True,
    'depth': None,
    'limit': 20,
    'whitelist': [
        re.compile(r'^https://timcast.com/members-area/section/timcast-irl/'),
        re.compile(r'^https://timcast.com/members-area/.*member-podcast'),
    ],
    'login': {
        'url': 'https://timcast.com/login/',
        'username': ['#user_login', TIMCAST_USERNAME],
        'password': ['#user_pass', TIMCAST_PASSWORD],
        'submit': '#wp-submit',
    },
}

videos = download(
    'Timcast IRL',
    'https://timcast.com/members-area/section/timcast-irl/',
    options,
)

pprint([v for v in videos])
