
# -*- coding: utf-8 -*-
import os
from six.moves.urllib.parse import urljoin
import requests


class Stockfighter(object):
    base_url = 'https://api.stockfighter.io/ob/api/'