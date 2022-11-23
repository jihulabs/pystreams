#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stockfighter
----------------------------------

Tests for `stockfighter` module.
"""
import os
import pytest
from stockfighter.stockfighter import Stockfighter

@pytest.fixture
def client():
    return Stockfighter(
        venue='TESTEX',
        account='EXB123456',
    )
STOCK = 'FOOBAR'


def test_heartbeat(client):
    assert client.heartbeat() is True

def test_venue_healthcheck(client):
  