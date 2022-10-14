
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

        https://starfighter.readme.io/docs/venue-healthcheck
        """
        url = urljoin(self.base_url, 'venues/TESTEX/heartbeat')
        return self.session.get(url).json()['ok']

    def venue_stocks(self):
        """List the stocks available for trading on the venue.

        https://starfighter.readme.io/docs/list-stocks-on-venue
        """
        url = urljoin(self.base_url, 'venues/{0}/stocks'.format(self.venue))
        return self.session.get(url).json()

    def orderbook_for_stock(self, stock):
        """Get the orderbook for a particular stock.

        https://starfighter.readme.io/docs/get-orderbook-for-stock
        """
        url_fragment = 'venues/{venue}/stocks/{stock}'.format(
            venue=self.venue,
            stock=stock,
        )
        url = urljoin(self.base_url, url_fragment)
        return self.session.get(url).json()

    def place_new_order(self, stock, price, qty, direction, order_type):
        """Place an order for a stock.

        https://starfighter.readme.io/docs/place-new-order
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/orders'.format(
            venue=self.venue,
            stock=stock,
        )
        data = {
          "stock": stock,
          "price": price,
          "venue": self.venue,
          "account": self.account,
          "qty": qty,
          "direction": direction,
          "orderType": order_type,
        }
        url = urljoin(self.base_url, url_fragment)
        resp = self.session.post(url, json=data)
        return resp.json()

    def quote_for_stock(self, stock):
        """Get a quick look at the most recent trade information for a stock.

        https://starfighter.readme.io/docs/a-quote-for-a-stock
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/quote'.format(
            venue=self.venue,
            stock=stock,
        )
        url = urljoin(self.base_url, url_fragment)
        return self.session.get(url).json()

    def status_for_order(self, order_id, stock):
        """Status For An Existing Order

        https://starfighter.readme.io/docs/status-for-an-existing-order
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/orders/{order_id}'.format(