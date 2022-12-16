"""MoabDB API Library"""

from typing import Union
import io
import concurrent.futures as cf
import pandas as pd


from . import constants
from . import proto_wrapper
from . import errors
from . import timewindows


def _check_access() -> bool:
    """
    Checks if the user has set the global credentials.
    This function is just a local sanity check, the server will
    check the credentials again.

    Returns:
        bool: True if the user has logged in
    """
    return not (constants.API_KEY == "" or constants.API_USERNAME == "")


def _server_req(ticker, start, end, datatype) -> pd.DataFrame:
    """
    Creates a high level request and parses the response

    Args:
        ticker (str): The ticker to query from the database
        start (int): The unix epoch time to start the query from
        end (int): The unix epoch time to stop searching at
        datatype (str): The data type that's being requested

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response
        errors.MoabRequestError: If the server has a problem interpreting the request
        errors.MoabInternalError: If the server runs into an unrecoverable error internally
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype
        errors.MoabNotFoundError: If the data requested wasn't found
        errors.MoabUnknownError: If the error code couldn't be parsed

    Returns:
        DataFrame: A Pandas DataFrame of the returned data

    """
    # Request data from moabdb server
    req = proto_wrapper.REQUEST()
    req.symbol = ticker
    req.start = start
    req.end = end
    req.datatype = datatype

    if constants.API_KEY != "":
        req.token = constants.API_KEY
        req.username = constants.API_USERNAME

    res = req.send(constants.DB_URL + 'request/v1/')

    res.throw()

    # Place data into a dataframe
    pq_file = io.BytesIO(res.data)
    try:
        d_f = pd.read_parquet(pq_file)
        return d_f
    except Exception as exc:
        raise errors.MoabResponseError("Server returned invalid data") from exc


def get_equity(tickers: Union[str, list], sample: str = "1m",
               start: str = None, end: str = None,
               intraday: bool = False) -> pd.DataFrame:
    """
    Gets equity data from the MoabDB API

    Args:
        tickers (Union[str, list]): The ticker(s) to look up
        sample (:obj:`str`, optional): Sample length, required if "start" or "end" is missing
        start (:obj:`str`, optional): Beginning date of sample,
            required if "end" or "sample" is missing
        end (:obj:`str`, optional): Ending date of sample,
            required if "start" or "sample" is missing
        intraday (:obj:`bool`, optional): True to return intraday data
            Default is 'False' to return end-of-day data
            See moabdb.com to look at subscriptions for intraday access

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response
        errors.MoabRequestError: If the server has a problem interpreting the request,
            or if an invalid parameter is passed
        errors.MoabInternalError: If the server runs into an unrecoverable error internally
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype
        errors.MoabNotFoundError: If the data requested wasn't found
        errors.MoabUnknownError: If the error code couldn't be parsed

    Returns:
        DataFrame: A Pandas DataFrame of the returned data

    Examples:

        Request the last year of Apple's daily data::

            import moabdb as mdb
            df = mdb.get_equity("AAPL", "1y")

        Request data for a list of symbols::

            import moabdb as mdb
            df = mdb.get_equity(["AMZN", "MSFT", "TSLA"], "1y")

        Request a specific month of Amazon daily data::

            import moabdb as mdb
            df = mdb.get_equity("AMZN", start="2022-04-01", sample="1m")

        Request intraday data of Tesla for the last month::

            import moabdb as mdb
            mdb.login("your_email@mail.com", "secret_key")
            df = mdb.get_equity("TSLA", "1m", intraday=True)
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

    # List of tickers request
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

    return return_db


def get_treasuries(sample: str = "1y",
                   start: str = None, end: str = None):
    """
    Gets equity data from the MoabDB API

    Args:
        sample (:obj:`str`, optional): Sample length, required if "start" or "end" is missing
        start (:obj:`str`, optional): Beginning date of sample,
            required if "end" or "sample" is missing
        end (:obj:`str`, optional): Ending date of sample,
            required if "start" or "sample" is missing

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response
        errors.MoabRequestError: If the server has a problem interpreting the request,
            or if an invalid parameter is passed
        errors.MoabInternalError: If the server runs into an unrecoverable error internally
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype
        errors.MoabNotFoundError: If the data requested wasn't found
        errors.MoabUnknownError: If the error code couldn't be parsed

    Returns:
        DataFrame: A Pandas DataFrame of the returned data

    Examples:

        Request the last year of treasuries data::

            import moabdb as mdb
            mdb.login("your_email@mail.com", "secret_key")
            df = mdb.get_treasuries("1y")

        Request a specific month of data::

            import moabdb as mdb
            mdb.login("your_email@mail.com", "secret_key")
            df = mdb.get_treasuries(start="2022-04-01", sample="1m")

    """

    # Check authorization
    if not _check_access():
        raise errors.MoabRequestError(
            "Premium datasets needs API credentials, see moabdb.com")

    # String time to integer time
    start_tm, end_tm = timewindows.get_unix_dates(sample, start, end)

    # Request treasury data
    columns = constants.TREASURY_COLUMNS
    return_db = _server_req("INTERNAL_TREASURY",
                            start_tm, end_tm, "treasuries")
    return return_db[columns]
