
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update encrypted deploy password in Travis config file
"""


from __future__ import print_function
import base64
import json
import os
from getpass import getpass
import yaml
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15


try:
    from urllib import urlopen
except:
    from urllib.request import urlopen


GITHUB_REPO = 'striglia/stockfighter'
TRAVIS_CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '.travis.yml')


def load_key(pubkey):
    """Load public RSA key, with work-around for keys using
    incorrect header/footer format.

    Read more about RSA encryption with cryptography:
    https://cryptography.io/latest/hazmat/primitives/asymmetric/rsa/
    """
    try:
        return load_pem_public_key(pubkey.encode(), default_backend())
    except ValueError:
        # workaround for https://github.com/travis-ci/travis-api/issues/196
        pubkey = pubkey.replace('BEGIN RSA', 'BEGIN').replace('END RSA', 'END')
        return load_pem_public_key(pubkey.encode(), default_backend())


def encrypt(pubkey, password):
    """Encrypt password using given RSA public key and encode it with base64.

    The encrypted password can only be decrypted by someone with the
    private key (in this case, only Travis).
    """
    key = load_key(pubkey)
    encrypted_password = key.encrypt(password, PKCS1v15())
    return base64.b64encode(encrypted_password)

