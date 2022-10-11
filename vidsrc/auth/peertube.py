import logging
from urllib.parse import urljoin

import requests


LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())


class PeerTubeAuth:
    def __init__(self, url):
        self.url = url

    def login(self, credentials):
        LOGGER.debug(credentials)
        r = requests.get(urljoin(self.url, '/api/v1/oauth-clients/local/'))
        params = r.json()
        r = requests.post(urljoin(self.url, '/api/v1/users/token/'), data={
            'client_id': params['client_id'],
            'client_secret': params['client_secret'],
            'grant_type': 'password',
            'username': credentials['username'],
            'password': credentials['password'],
        })
        token = r.json()
        return {
            'headers': {
                'Authorization': f"Bearer {token['access_token']}"
            }
        }
