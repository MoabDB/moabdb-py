Financial Statements
####################


Return a ``pandas.DataFrame`` of historical price and volume information
for the ticker(s) provided.

This function can be modified to pull daily-level data or intraday
second-level data. Daily data reflects market trades between 9:30 AM
and 4:00 PM, Eastern. Intraday data reflects market trades between
8:00 AM and 6:00 PM, Eastern.


Parameters
----------
tickers : str or list of str
   The ticker(s) to look up. It can be a single ticker symbol (str)
   or a list of ticker symbols (list of str).

sample : str, optional
   Sample period length. Can be used alone or with ``start`` | ``end``.

start : str, optional
   Sample start date. Requires one of ``end`` or ``sample``.

end : str, optional
   Sample end date. Requires one of ``start`` or ``sample``.

intraday : bool, optional, default False
   Set to ``True`` to return intraday data.
   Default is ``False`` to return end-of-day data.
   See moabdb.com for subscriptions for intraday access.

.. note::
   - ``sample`` can be used alone to return the most recent data,
      but ``start`` and ``end`` require two arguments
      from ``sample`` | ``start`` | ``end``.


Returns
-------
out : pandas.DataFrame
   DataFrame containing equity price and volume information, indexed by datetime64.

   **Daily Data Columns:**

   +-----------------------+--------------------------------------------+
   | Column variable       | Variable Description                       |
   +=======================+============================================+
   | ``Symbol`` (str)      | Ticker symbol of the equity.               |
   +-----------------------+--------------------------------------------+
   | ``Open`` (float)      | Opening trade price.                       |
   +-----------------------+--------------------------------------------+
   | ``High`` (float)      | Highest trade price.                       |
   +-----------------------+--------------------------------------------+
   | ``Low`` (float)       | Lowest trade price.                        |
   +-----------------------+--------------------------------------------+
   | ``Close`` (float)     | Closing trade price.                       |
   +-----------------------+--------------------------------------------+
   | ``VWAP`` (float)      | Volume-weighted average price.             |
   +-----------------------+--------------------------------------------+
   | ``BidPrc`` (float)    | Bid price.                                 |
   +-----------------------+--------------------------------------------+
   | ``AskPrc`` (float)    | Ask price.                                 |
   +-----------------------+--------------------------------------------+
   | ``Volume`` (int)      | Volume traded.                             |
   +-----------------------+--------------------------------------------+
   | ``Trades`` (int)      | Number of trades.                          |
   +-----------------------+--------------------------------------------+

   **Intraday Data Columns:**

   +-----------------------+--------------------------------------------------+
   | Column variable       | Variable Description                             |
   +=======================+==================================================+
   | ``Symbol`` (str)      | Ticker symbol of the equity.                     |
   +-----------------------+--------------------------------------------------+
   | ``Trades`` (int)      | Number of trades.                                |
   +-----------------------+--------------------------------------------------+
   | ``Volume`` (int)      | Volume traded.                                   |
   +-----------------------+--------------------------------------------------+
   | ``Imbalance`` (int)   | Buy-initiated volume minus sell-initiated volume.|
   +-----------------------+--------------------------------------------------+
   | ``Close`` (float)     | Closing trade price.                             |
   +-----------------------+--------------------------------------------------+
   | ``VWAP`` (float)      | Volume-weighted average price.                   |
   +-----------------------+--------------------------------------------------+
   | ``BidPrc`` (float)    | Bid price.                                       |
   +-----------------------+--------------------------------------------------+
   | ``AskPrc`` (float)    | Ask price.                                       |
   +-----------------------+--------------------------------------------------+
   | ``BidSz`` (int)       | Round lots available at BidPrc.                  |
   +-----------------------+--------------------------------------------------+
   | ``AskSz`` (int)       | Round lots available at AskPrc.                  |
   +-----------------------+--------------------------------------------------+

.. note::

   - If the request is for a single ticker, the DataFrame will be returned
      with single index columns.

   - If the request is for multiple tickers, the DataFrame will be returned
      with multi-index columns, with the first level being the ticker symbol.


Examples
--------
**Request the last year of ``AAPL`` daily data:**

>>> import moabdb as mdb
>>> df = mdb.get_equity("AAPL", "1y")

**Request the most recent year of daily equity data for multiple stocks:**

>>> df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

**Request a specific month of daily data:**

>>> df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

**Request daily data between two specific dates:**
>>> df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")

**Request the most recent month of intraday data:**
>>> mdb.login("your_email@example.com", "moabdb_api_key")
>>> df = mdb.get_equity("TSLA", "1m", intraday=True)

**Request intraday data between two specific dates:**
>>> mdb.login("your_email@example.com", "moabdb_api_key")
>>> df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)


Raises
------
errors.MoabResponseError:
   If there's a problem interpreting the response
errors.MoabRequestError:
   If the server has a problem interpreting the request,
   or if an invalid parameter is passed
errors.MoabInternalError:
   If the server runs into an unrecoverable error internally
errors.MoabHttpError:
   If there's a problem transporting the payload or receiving a response
errors.MoabUnauthorizedError:
   If the user is not authorized to request the datatype
errors.MoabNotFoundError:
   If the data requested wasn't found
errors.MoabUnknownError:
   If the error code couldn't be parsed


+-----------------------+--------------------------------------------------+
| Column variable       | Variable Description                             |
+=======================+==================================================+
| ``Symbol`` (str)      | Ticker symbol of the equity.                     |
+-----------------------+--------------------------------------------------+
| ``Time`` (datetime64) | Time of the data point.                          |
+-----------------------+--------------------------------------------------+
| ``Trades`` (int)      | Number of trades.                                |
+-----------------------+--------------------------------------------------+
| ``Volume`` (int)      | Volume traded.                                   |
+-----------------------+--------------------------------------------------+
| ``Imbalance`` (int)   | Buy-initiated volume minus sell-initiated volume.|
+-----------------------+--------------------------------------------------+
| ``Close`` (float)     | Closing trade price.                             |
+-----------------------+--------------------------------------------------+
| ``VWAP`` (float)      | Volume-weighted average price.                   |
+-----------------------+--------------------------------------------------+
| ``BidPrc`` (float)    | Bid price.                                       |
+-----------------------+--------------------------------------------------+
| ``AskPrc`` (float)    | Ask price.                                       |
+-----------------------+--------------------------------------------------+
| ``BidSz`` (int)       | Round lots available at BidPrc.                  |
+-----------------------+--------------------------------------------------+
| ``AskSz`` (int)       | Round lots available at AskPrc.                  |
+-----------------------+--------------------------------------------------+

+-------------------------+--------------------------------------------------+
| Column variable         | Variable Description                             |
+=========================+==================================================+
| ``Symbol`` (str)        | Ticker symbol of the equity.                     |
| ``Time`` (datetime64)   | Time of the data point.                          |
| ``Trades`` (int)        | Number of trades.                                |
| ``Volume`` (int)        | Volume traded.                                   |
| ``Imbalance`` (int)     | Buy-initiated volume minus sell-initiated volume.|
| ``Close`` (float)       | Closing trade price.                             |
| ``VWAP`` (float)        | Volume-weighted average price.                   |
| ``BidPrc`` (float)      | Bid price.                                       |
| ``AskPrc`` (float)      | Ask price.                                       |
| ``BidSz`` (int)         | Round lots available at BidPrc.                  |
| ``AskSz`` (int)         | Round lots available at AskPrc.                  |
+-------------------------+--------------------------------------------------+

+-------------------+--------------------------------------------------+
| Column variable   | Variable Description                             |
+===================+==================================================+
| Symbol (str)      | Ticker symbol of the equity.                     |
| Time (datetime64) | Time of the data point.                          |
| Trades (int)      | Number of trades.                                |
| Volume (int)      | Volume traded.                                   |
| Imbalance (int)   | Buy-initiated volume minus sell-initiated volume.|
| Close (float)     | Closing trade price.                             |
| VWAP (float)      | Volume-weighted average price.                   |
| BidPrc (float)    | Bid price.                                       |
| AskPrc (float)    | Ask price.                                       |
| BidSz (int)       | Round lots available at BidPrc.                  |
| AskSz (int)       | Round lots available at AskPrc.                  |
+-------------------+--------------------------------------------------+

+-----------------------------+----------------------------------------------------+
| Column variable             | Variable Description                               |
+=============================+====================================================+
| | ``Symbol`` (str)          | | Ticker symbol of the equity.                     |
| | ``Time`` (datetime64)     | | Time of the data point.                          |
| | ``Trades`` (int)          | | Number of trades.                                |
| | ``Volume`` (int)          | | Volume traded.                                   |
| | ``Imbalance`` (int)       | | Buy-initiated volume minus sell-initiated volume.|
| | ``Close`` (float)         | | Closing trade price.                             |
| | ``VWAP`` (float)          | | Volume-weighted average price.                   |
| | ``BidPrc`` (float)        | | Bid price.                                       |
| | ``AskPrc`` (float)        | | Ask price.                                       |
| | ``BidSz`` (int)           | | Round lots available at BidPrc.                  |
| | ``AskSz`` (int)           | | Round lots available at AskPrc.                  |
+-----------------------------+----------------------------------------------------+

.. automodule:: moabdb.get_rates.get_rates
   :members:
   :undoc-members:
   :show-inheritance: