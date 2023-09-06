.. _get-rates-ref:

``get_rates()``
###############

Retrieving Interest Rates
=========================

.. automodule:: moabdb
   :members: get_rates


Login Example
=============

.. Example 1

**Import the library**

>>> import moabdb as mdb

**Login for intraday data requests**

>>> mdb.login("your_email@example.com", "moabdb_api_key")

Request the most recent month of intraday data.

>>> df = mdb.get_equity("TSLA", "1m", intraday=True)


Request intraday data between two specific dates:**

>>> df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)
