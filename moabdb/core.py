#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# moabdb - Online finance database
# https://github.com/MoabDB
# https://moabdb.com
# Copyright 2022-2023
#


"""
The `get_equity` function provides access to historical price and volume
information for equities from the Moab Database (moabdb.com). It allows users
to request both daily-level and intraday-level data for one or multiple ticker
symbols.

All data retrieved using the ``moabdb`` module are returned as pandas DataFrames.

Usage
-----
Import the module and use the available functions to fetch equity and rates data:

>>> import moabdb as mdb
>>> df = mdb.get_equity("AAPL", "6m") # Get 6 months of AAPL daily data

To access intraday data, you must first login with your API credentials:

>>> import moabdb as mdb
>>> mdb.login("your_email@example.com", "moabdb_api_key")
>>> df = mdb.get_equity("AAPL", "6m") # Get 6 months of AAPL intraday data



For information on subscriptions visit https://moabdb.com.

To view the source code visit https://github.com/MoabDB.

"""

from . import constants
from . import errors
from . import timewindows
from .lib import _check_access, _server_req
from .constants import pd, Union, cf



def get_equity(tickers: Union[str, list],
               sample: str = "1m",
               start: str = None,
               end: str = None,
               intraday: bool = False) -> pd.DataFrame:
    """

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
        The format of the DataFrame depends on the request type.

        If the request is for a single ticker, the DataFrame will be returned with single
        index.If the request is for multiple tickers, the DataFrame will be returned
        with multi-index columns, with the first level being the ticker symbol.

        **If the request is for daily data, the DataFrame will contain the following columns:**

        +-----------------------+--------------------------------------------+
        | DataFrame Columns     | Column Description                         |
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

        **If the request is for intraday data, the DataFrame will contain the following columns:**

        +-----------------------+--------------------------------------------------+
        | DataFrame Columns     | Column Description                               |
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

    **Import the library**

    >>> import moabdb as mdb


    Request the last year of ``AAPL`` daily data.

    >>> df = mdb.get_equity("AAPL", "1y")


    Request the most recent year of daily equity data for multiple stocks.

    >>> df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")


    Request a specific month of daily data.

    >>> df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")


    Request daily data between two specific dates.

    >>> df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")


    **Login for intraday data requests**

    >>> mdb.login("your_email@example.com", "moabdb_api_key")


    Request the most recent month of intraday data.

    >>> df = mdb.get_equity("TSLA", "1m", intraday=True)


    Request intraday data between two specific dates:**

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


    """

    # Check intraday authorization
    if intraday is True:
        equity_freq = "intraday_stocks"
        columns = constants.INTRA_COLUMNS
        if not _check_access():
            raise errors.MoabRequestError(
                "Intraday needs API credentials, see moabdb.com")
    else:
        equity_freq = "daily_stocks"
        columns = constants.DAILY_COLUMNS

    # String time to integer time
    start_tm, end_tm = timewindows.get_unix_dates(sample, start, end)

    # Single ticker request
    if isinstance(tickers, str):
        return_db = _server_req(
            str.upper(tickers), start_tm, end_tm, equity_freq)
        return_db = return_db[columns]
        return_db = return_db.set_index(columns[1])

    # Multiple tickers request
    elif isinstance(tickers, list):
        processed = []
        calls = len(tickers)
        with cf.ThreadPoolExecutor() as pool:
            for result in pool.map(_server_req, tickers, [start_tm]*calls,
                                   [end_tm]*calls, [equity_freq]*calls):
                processed.append(result)
        return_db = pd.concat(processed)[columns]
        return_db = return_db.set_index(columns[0:2]).unstack(0)

    # Unknown ticker request
    else:
        raise errors.MoabRequestError("Invalid window type")

    # Round float columns
    float_columns = return_db.select_dtypes(include=['float32', 'float64'])
    if float_columns.size > 0:
        return_db[float_columns.columns] = float_columns.astype(
            'float64').round(4)

    return return_db


def get_rates(sample: str = "1y",
              start: str = None,
              end: str = None) -> pd.DataFrame:
    """
    Gets treasury data from the MoabDB API.

    Args:
        sample (str, optional): Sample length, required if "start" or "end" is missing.
        start (str, optional): Beginning date of sample, required if "end" or "sample" is missing.
        end (str, optional): Ending date of sample, required if "start" or "sample" is missing.

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response.
        errors.MoabRequestError: If the server has a problem interpreting the request,
            or if an invalid parameter is passed.
        errors.MoabInternalError: If the server runs into an unrecoverable error internally.
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response.
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype.
        errors.MoabNotFoundError: If the data requested wasn't found.
        errors.MoabUnknownError: If the error code couldn't be parsed.

    Returns:
        pandas.DataFrame: A DataFrame containing daily treasury data.
            Index: Date (datetime64): Date of the data point as YYYY-MM-DD.
            Columns:
                - Treasury_1m (float): Treasury yield for a 1-month maturity.
                - Treasury_2m (float): Treasury yield for a 2-month maturity.
                - Treasury_3m (float): Treasury yield for a 3-month maturity.
                - Treasury_4m (float): Treasury yield for a 4-month maturity.
                - Treasury_6m (float): Treasury yield for a 6-month maturity.
                - Treasury_1y (float): Treasury yield for a 1-year maturity.
                - Treasury_2y (float): Treasury yield for a 2-year maturity.
                - Treasury_3y (float): Treasury yield for a 3-year maturity.
                - Treasury_5y (float): Treasury yield for a 5-year maturity.
                - Treasury_7y (float): Treasury yield for a 7-year maturity.
                - Treasury_10y (float): Treasury yield for a 10-year maturity.
                - Treasury_20y (float): Treasury yield for a 20-year maturity.
                - Treasury_30y (float): Treasury yield for a 30-year maturity.
                - Realrate_5y (float): Real interest rate for a 5-year maturity.
                - Realrate_7y (float): Real interest rate for a 7-year maturity.
                - Realrate_10y (float): Real interest rate for a 10-year maturity.
                - Realrate_20y (float): Real interest rate for a 20-year maturity.
                - Realrate_30y (float): Real interest rate for a 30-year maturity.

    Examples:

        - Request the last year of treasury data:
            import moabdb as mdb
            df = mdb.get_rates("1y")

        - Request a specific month of data:
            import moabdb as mdb
            df = mdb.get_rates(start="2022-04-01", sample="1m")

        - Request treasury data for a specific date range:
            import moabdb as mdb
            df = mdb.get_rates(start="2020-01-01", end="2020-12-31")

    """

    # Check authorization
    if not _check_access():
        raise errors.MoabRequestError(
            "Premium datasets needs API credentials, see moabdb.com")

    # String time to integer time
    start_tm, end_tm = timewindows.get_unix_dates(sample, start, end)

    # Request treasury data
    columns = constants.RATES_COLUMNS
    return_db = _server_req("INTERNAL_TREASURY",
                            start_tm, end_tm, "treasuries")

    # Format treasury data
    return_db = return_db[columns].set_index(columns[0])

    return return_db
