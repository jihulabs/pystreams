
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