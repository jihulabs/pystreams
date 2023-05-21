
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