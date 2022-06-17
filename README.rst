===============================
Stockfighter
===============================

.. image:: https://badges.gitter.im/striglia/stockfighter.svg
   :alt: Join the chat at https://gitter.im/striglia/stockfighter
   :target: https://gitter.im/striglia/stockfighter?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://img.shields.io/pypi/v/stockfighter.svg
        :target: https://pypi.python.org/pypi/stockfighter

.. image:: https://img.shields.io/travis/striglia/stockfighter.svg
        :target: https://travis-ci.org/striglia/stockfighter

.. image:: https://readthedocs.org/projects/stockfighter/badge/?version=latest
        :target: https://readthedocs.org/projects/stockfighter/?badge=latest
        :alt: Documentation Status


API wrapper for Stockfighter

* Free software: ISC license
* Limited documentation exists at: https://stockfighter.readthedocs.org. Happily accepting patches to improve it!

Get things started
--------------------

Not hard!

.. code-block:: shell

    pip install stockfighter

Using the standard API

.. code-block:: python

    from stockfighter import Stockfighter
    s = Stockfighter(venue='TESTEX', account='EXB123456', api_key='123456')
    print(s.venue_stocks())

...and the GM API for managing levels and such

.. code-block:: python

    from stockfighter import GM
    gm = GM(api_key=123456)
    print gm.start('first_steps')  # Start the first level programmatically

For simplicity (and so you can share your code!) the GM and 