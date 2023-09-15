``get_cf()``
############

Coming soon, undergoing alpha testing

.. Examples
.. --------

.. .. code-block:: python
..    :linenos:

..    import moabdb as mdb
   
..    # -- Pulling daily data -- #

..    #Request the last year of ``AAPL`` daily data:
..    df = mdb.get_equity("AAPL", "1y")

..    # Request the most recent year of daily equity data for multiple stocks:
..    df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

..    # Request a specific month of daily data:
..    df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

..    # Request daily data between two specific dates:
..    df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")


..    # -- Pulling intraday data -- #

..    mdb.login("your_email@example.com", "moabdb_api_key")
   
..    # Request the most recent month of intraday data:
..    df = mdb.get_equity("TSLA", "1m", intraday=True)

..    # Request intraday data between two specific dates:
..    df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)



.. Returns
.. -------
.. out : pandas.DataFrame
..    DataFrame containing equity price and volume information, indexed by datetime64.

..    **Daily Data Columns:**

..    +-----------------------+--------------------------------------------+
..    | Column variable       | Variable Description                       |
..    +=======================+============================================+
..    | ``Symbol`` (str)      | Ticker symbol of the equity.               |
..    +-----------------------+--------------------------------------------+
..    | ``Open`` (float)      | Opening trade price.                       |
..    +-----------------------+--------------------------------------------+
..    | ``High`` (float)      | Highest trade price.                       |
..    +-----------------------+--------------------------------------------+
..    | ``Low`` (float)       | Lowest trade price.                        |
..    +-----------------------+--------------------------------------------+
..    | ``Close`` (float)     | Closing trade price.                       |
..    +-----------------------+--------------------------------------------+
..    | ``VWAP`` (float)      | Volume-weighted average price.             |
..    +-----------------------+--------------------------------------------+
..    | ``BidPrc`` (float)    | Bid price.                                 |
..    +-----------------------+--------------------------------------------+
..    | ``AskPrc`` (float)    | Ask price.                                 |
..    +-----------------------+--------------------------------------------+
..    | ``Volume`` (int)      | Volume traded.                             |
..    +-----------------------+--------------------------------------------+
..    | ``Trades`` (int)      | Number of trades.                          |
..    +-----------------------+--------------------------------------------+

..    **Intraday Data Columns:**

..    +-----------------------+--------------------------------------------------+
..    | Column variable       | Variable Description                             |
..    +=======================+==================================================+
..    | ``Symbol`` (str)      | Ticker symbol of the equity.                     |
..    +-----------------------+--------------------------------------------------+
..    | ``Trades`` (int)      | Number of trades.                                |
..    +-----------------------+--------------------------------------------------+
..    | ``Volume`` (int)      | Volume traded.                                   |
..    +-----------------------+--------------------------------------------------+
..    | ``Imbalance`` (int)   | Buy-initiated volume minus sell-initiated volume.|
..    +-----------------------+--------------------------------------------------+
..    | ``Close`` (float)     | Closing trade price.                             |
..    +-----------------------+--------------------------------------------------+
..    | ``VWAP`` (float)      | Volume-weighted average price.                   |
..    +-----------------------+--------------------------------------------------+
..    | ``BidPrc`` (float)    | Bid price.                                       |
..    +-----------------------+--------------------------------------------------+
..    | ``AskPrc`` (float)    | Ask price.                                       |
..    +-----------------------+--------------------------------------------------+
..    | ``BidSz`` (int)       | Round lots available at BidPrc.                  |
..    +-----------------------+--------------------------------------------------+
..    | ``AskSz`` (int)       | Round lots available at AskPrc.                  |
..    +-----------------------+--------------------------------------------------+

.. .. note::

..    - If the request is for a single ticker, the DataFrame will be returned
..       with single index columns.

..    - If the request is for multiple tickers, the DataFrame will be returned
..       with multi-index columns, with the first level being the ticker symbol.


.. Examples
.. --------
.. **Request the last year of ``AAPL`` daily data:**

.. >>> import moabdb as mdb
.. >>> df = mdb.get_equity("AAPL", "1y")

.. **Request the most recent year of daily equity data for multiple stocks:**

.. >>> df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

.. **Request a specific month of daily data:**

.. >>> df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

.. **Request daily data between two specific dates:**
.. >>> df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")

.. **Request the most recent month of intraday data:**
.. >>> mdb.login("your_email@example.com", "moabdb_api_key")
.. >>> df = mdb.get_equity("TSLA", "1m", intraday=True)

.. **Request intraday data between two specific dates:**
.. >>> mdb.login("your_email@example.com", "moabdb_api_key")
.. >>> df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)


.. Raises
.. ------
.. errors.MoabResponseError:
..    If there's a problem interpreting the response
.. errors.MoabRequestError:
..    If the server has a problem interpreting the request,
..    or if an invalid parameter is passed
.. errors.MoabInternalError:
..    If the server runs into an unrecoverable error internally
.. errors.MoabHttpError:
..    If there's a problem transporting the payload or receiving a response
.. errors.MoabUnauthorizedError:
..    If the user is not authorized to request the datatype
.. errors.MoabNotFoundError:
..    If the data requested wasn't found
.. errors.MoabUnknownError:
..    If the error code couldn't be parsed


.. +-----------------------+--------------------------------------------------+
.. | Column variable       | Variable Description                             |
.. +=======================+==================================================+
.. | ``Symbol`` (str)      | Ticker symbol of the equity.                     |
.. +-----------------------+--------------------------------------------------+
.. | ``Time`` (datetime64) | Time of the data point.                          |
.. +-----------------------+--------------------------------------------------+
.. | ``Trades`` (int)      | Number of trades.                                |
.. +-----------------------+--------------------------------------------------+
.. | ``Volume`` (int)      | Volume traded.                                   |
.. +-----------------------+--------------------------------------------------+
.. | ``Imbalance`` (int)   | Buy-initiated volume minus sell-initiated volume.|
.. +-----------------------+--------------------------------------------------+
.. | ``Close`` (float)     | Closing trade price.                             |
.. +-----------------------+--------------------------------------------------+
.. | ``VWAP`` (float)      | Volume-weighted average price.                   |
.. +-----------------------+--------------------------------------------------+
.. | ``BidPrc`` (float)    | Bid price.                                       |
.. +-----------------------+--------------------------------------------------+
.. | ``AskPrc`` (float)    | Ask price.                                       |
.. +-----------------------+--------------------------------------------------+
.. | ``BidSz`` (int)       | Round lots available at BidPrc.                  |
.. +-----------------------+--------------------------------------------------+
.. | ``AskSz`` (int)       | Round lots available at AskPrc.                  |
.. +-----------------------+--------------------------------------------------+

.. +-------------------------+--------------------------------------------------+
.. | Column variable         | Variable Description                             |
.. +=========================+==================================================+
.. | ``Symbol`` (str)        | Ticker symbol of the equity.                     |
.. | ``Time`` (datetime64)   | Time of the data point.                          |
.. | ``Trades`` (int)        | Number of trades.                                |
.. | ``Volume`` (int)        | Volume traded.                                   |
.. | ``Imbalance`` (int)     | Buy-initiated volume minus sell-initiated volume.|
.. | ``Close`` (float)       | Closing trade price.                             |
.. | ``VWAP`` (float)        | Volume-weighted average price.                   |
.. | ``BidPrc`` (float)      | Bid price.                                       |
.. | ``AskPrc`` (float)      | Ask price.                                       |
.. | ``BidSz`` (int)         | Round lots available at BidPrc.                  |
.. | ``AskSz`` (int)         | Round lots available at AskPrc.                  |
.. +-------------------------+--------------------------------------------------+

.. +-------------------+--------------------------------------------------+
.. | Column variable   | Variable Description                             |
.. +===================+==================================================+
.. | Symbol (str)      | Ticker symbol of the equity.                     |
.. | Time (datetime64) | Time of the data point.                          |
.. | Trades (int)      | Number of trades.                                |
.. | Volume (int)      | Volume traded.                                   |
.. | Imbalance (int)   | Buy-initiated volume minus sell-initiated volume.|
.. | Close (float)     | Closing trade price.                             |
.. | VWAP (float)      | Volume-weighted average price.                   |
.. | BidPrc (float)    | Bid price.                                       |
.. | AskPrc (float)    | Ask price.                                       |
.. | BidSz (int)       | Round lots available at BidPrc.                  |
.. | AskSz (int)       | Round lots available at AskPrc.                  |
.. +-------------------+--------------------------------------------------+

.. +-----------------------------+----------------------------------------------------+
.. | Column variable             | Variable Description                               |
.. +=============================+====================================================+
.. | | ``Symbol`` (str)          | | Ticker symbol of the equity.                     |
.. | | ``Time`` (datetime64)     | | Time of the data point.                          |
.. | | ``Trades`` (int)          | | Number of trades.                                |
.. | | ``Volume`` (int)          | | Volume traded.                                   |
.. | | ``Imbalance`` (int)       | | Buy-initiated volume minus sell-initiated volume.|
.. | | ``Close`` (float)         | | Closing trade price.                             |
.. | | ``VWAP`` (float)          | | Volume-weighted average price.                   |
.. | | ``BidPrc`` (float)        | | Bid price.                                       |
.. | | ``AskPrc`` (float)        | | Ask price.                                       |
.. | | ``BidSz`` (int)           | | Round lots available at BidPrc.                  |
.. | | ``AskSz`` (int)           | | Round lots available at AskPrc.                  |
.. +-----------------------------+----------------------------------------------------+

.. .. .. automodule:: moabdb.get_rates.get_rates
..    :members:
..    :undoc-members:
..    :show-inheritance: