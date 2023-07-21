#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# moabdb - Online finance database
# https://github.com/MoabDB
# https://moabdb.com
# Copyright 2022-2023
#

"""
The get_equity() function for moabdb allows the user to
access historical daily and intraday equity data from the MoabDB API.
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
    Return an ndarray of the provided type that satisfies requirements.

    This function is useful to be sure that an array with the correct flags
    is returned for passing to compiled code (perhaps through ctypes).

    Parameters
    ----------
    a : array_like
       The object to be converted to a type-and-requirement-satisfying array.
    dtype : data-type
       The required data-type. If None preserve the current dtype. If your
       application requires the data to be in native byteorder, include
       a byteorder specification as a part of the dtype specification.
    requirements : str or sequence of str
       The requirements list can be any of the following

       * 'F_CONTIGUOUS' ('F') - ensure a Fortran-contiguous array
       * 'C_CONTIGUOUS' ('C') - ensure a C-contiguous array
       * 'ALIGNED' ('A')      - ensure a data-type aligned array
       * 'WRITEABLE' ('W')    - ensure a writable array
       * 'OWNDATA' ('O')      - ensure an array that owns its own data
       * 'ENSUREARRAY', ('E') - ensure a base array, instead of a subclass
    ${ARRAY_FUNCTION_LIKE}

        .. versionadded:: 1.20.0

    Returns
    -------
    out : ndarray
        Array with specified requirements and type if given.

    See Also
    --------
    asarray : Convert input to an ndarray.
    asanyarray : Convert to an ndarray, but pass through ndarray subclasses.
    ascontiguousarray : Convert input to a contiguous array.
    asfortranarray : Convert input to an ndarray with column-major
                     memory order.
    ndarray.flags : Information about the memory layout of the array.

    Notes
    -----
    The returned array will be guaranteed to have the listed requirements
    by making a copy if needed.

    Examples
    --------
    >>> x = np.arange(6).reshape(2,3)
    >>> x.flags
      C_CONTIGUOUS : True
      F_CONTIGUOUS : False
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False

    >>> y = np.require(x, dtype=np.float32, requirements=['A', 'O', 'W', 'F'])
    >>> y.flags
      C_CONTIGUOUS : False
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False

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
        return_db[float_columns.columns] = float_columns.astype('float64').round(4)

    return return_db

    # """
    # Function to retrieve equity data from the MoabDB API.

    # The get_equity() function can be used to access both historical daily and intraday data.

    # .. admonition:: Data Aggregation
    #     - Daily data: Returns a single data point per day based on activity \
    #         between 9:30 AM and 4:00 PM EST
    #     - Intraday data: Returns second-level aggregations for \
    #         market activity 8:00 AM and 6:00 PM EST


    # Parameters:
    # -----------
    # tickers : (Union[str, list])
    #     The ticker(s) to look up
    # sample : (str), optional
    #     The sample length, requires at least one of "start" or "end"
    # start : (str), optional
    #     The sample start date, requires at least one of "end" or "sample"
    # end : (str), optional
    #     The sample end date, requires at least one of "start" or "sample"
    # intraday : (bool), optional
    #     Set to `True` to return intraday data
    #     Default is "False" to return end-of-day data
    #     See moabdb.com for subscriptions for intraday access

    # Raises:
    # -------
    # errors.MoabResponseError:
    #     If there's a problem interpreting the response
    # errors.MoabRequestError:
    #     If the server has a problem interpreting the request,
    #     or if an invalid parameter is passed
    # errors.MoabInternalError:
    #     If the server runs into an unrecoverable error internally
    # errors.MoabHttpError:
    #     If there's a problem transporting the payload or receiving a response
    # errors.MoabUnauthorizedError:
    #     If the user is not authorized to request the datatype
    # errors.MoabNotFoundError:
    #     If the data requested wasn't found
    # errors.MoabUnknownError:
    #     If the error code couldn't be parsed

    # Returns:
    # -------
    # pandas.DataFrame:
    #     A DataFrame containing equity price and volume information.

    # For Daily data:
    #     Timeframe: Based on valid observations between 9:30 AM and 4:00 PM EST
    #     Index:
    #         - Date (datetime64): Day of observations formatted as "YYYY-MM-DD".
    #     Columns:
    #         - Symbol (str): Ticker symbol of the equity.
    #         - Open (float): Opening trade price.
    #         - High (float): Highest trade price.
    #         - Low (float): Lowest trade price.
    #         - Close (float): Closing trade price.
    #         - VWAP (float): Volume-weighted average price.
    #         - BidPrc (float): Bid price.
    #         - AskPrc (float): Ask price.
    #         - Volume (int): Volume traded.
    #         - Trades (int): Number of trades.

    # Intraday data:
    #     Timeframe: Valid observations between 8:00 AM and 6:00 PM EST
    #     Index:
    #         - Time (datetime64): Time of observation formatted as "YYYY-MM-DD HH:MM:SS".
    #     Columns:
    #         - Symbol (str): Ticker symbol of the equity.
    #         - Time (datetime64): Time of the data point.
    #         - Trades (int): Number of trades.
    #         - Volume (int): Volume traded.
    #         - Imbalance (int): Buy-initiated volume minus sell-initiated volume.
    #         - Close (float): Closing trade price.
    #         - VWAP (float): Volume-weighted average price.
    #         - BidPrc (float): Bid price.
    #         - AskPrc (float): Ask price.
    #         - BidSz (int): Round lots available at BidPrc.
    #         - AskSz (int): Round lots available at AskPrc.

    #     Note:
    #         - If the request is for a single ticker, the DataFrame will be returned
    #             with single index columns.
    #         - If the request is for multiple tickers, the DataFrame will be returned
    #             with multi-index columns, with the first level being the ticker symbol.


    # Examples:

    #     - Request the last year of Apple daily data:
    #         import moabdb as mdb
    #         df = mdb.get_equity("AAPL", "1y")

    #     - Request the most recent year of daily equity data for a multiple stocks:
    #         import moabdb as mdb
    #         df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

    #     - Request a specific month of daily data:
    #         import moabdb as mdb
    #         df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

    #      - Request daily data between specific dates:
    #         import moabdb as mdb
    #         df = mdb.get_equity("AMZN", start="2022-04-01", end="2022-10-01")

    #     - Request the most recent month of intraday data:
    #         import moabdb as mdb
    #         mdb.login("your_email@example.com", "moabdb_api_key")
    #         df = mdb.get_equity("TSLA", "1m", intraday=True)

    #     - Request intraday data between two specific dates:
    #         import moabdb as mdb
    #         mdb.login("your_email@example.com", "moabdb_api_key")
    #         df = mdb.get_equity("TSLA", start="2020-01-01", end="2020-06-01", intraday=True)

    # """
