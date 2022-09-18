
#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='stockfighter',
    version='0.2.7',
    description="API wrapper for Stockfighter",
    long_description=readme + '\n\n' + history,
    author="Scott Triglia",
    author_email='scott.triglia@gmail.com',
    url='https://github.com/striglia/stockfighter',
    packages=['stockfighter'],
    package_dir={'stockfighter': 'stockfighter'},
    include_package_data=True,
    install_requires=[
        'requests>=2.4.2',
        'six',