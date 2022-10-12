
import os
import requests
from six.moves.urllib.parse import urljoin


class GM(object):
    base_url = 'https://www.stockfighter.io/gm/'

    def __init__(self, api_key=None):
        self.api_key = os.environ['API_KEY'] if api_key is None else api_key
        self.headers = {'Cookie': 'api_key={api_key}'.format(api_key=self.api_key)}

        # Data on which levels you have running.
        self.level_data = self._load_data()

    def _load_data(self):
        """Internal method for querying the GM api for currently running levels
        and storing that state."""
        url = urljoin(self.base_url, 'levels')
        resp = requests.get(url, headers=self.headers)
        # TOOD: Confirm/deny that this is a real API for the levels currenlty running...
        if resp.content: