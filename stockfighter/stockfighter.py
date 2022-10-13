
# -*- coding: utf-8 -*-
import os
from six.moves.urllib.parse import urljoin
import requests


class Stockfighter(object):
    base_url = 'https://api.stockfighter.io/ob/api/'

    def __init__(self, venue, account, api_key=None):
        self.venue = venue
        self.account = account

        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.environ['API_KEY']

        self.session = requests.Session()
        self.session.headers.update({
            'X-Starfighter-Authorization': self.api_key
        })

    def heartbeat(self):
        """Check The API Is Up.

        https://starfighter.readme.io/docs/heartbeat
        """
        url = urljoin(self.base_url, 'heartbeat')
        return self.session.get(url).json()['ok']

    def venue_healthcheck(self):
        """Check A Venue Is Up.
