.. _get-equity-ref:

``get_equity()``
################

Retrieving Equity Prices
========================

.. note::
    See :ref:`equity-data-ref` for documentation about the dataset 
    and variables.


.. automodule:: moabdb
   :members: get_equity



Daily data examples, no login
=============================

.. Example 1
.. code-block:: python
    :linenos:

    import moabdb as mdb

    # Request the last year of ``AAPL`` daily data.
    df = mdb.get_equity("AAPL", "1y")

    # Request the most recent year of daily equity data for multiple stocks.
    df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

    # Request a specific month of daily data.
    df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

    # Request daily data between two specific dates.
    df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")


Intraday data examples, with login
==================================

**Login for intraday data requests**

>>> mdb.login("your_email@example.com", "moabdb_api_key")


Request the most recent month of intraday data.

>>> df = mdb.get_equity("TSLA", "1m", intraday=True)


Request intraday data between two specific dates:**

>>> df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)
