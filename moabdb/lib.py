"""MoabDB API Library"""

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
    """
    return not (constants.API_KEY == "" or constants.API_USERNAME == "")


def _server_req(ticker, start, end, datatype):
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


def get_equity(tickers, sample="1m",
               start=None, end=None,
               intraday=False):
    """
    get_equity paramaters:
        tickers: str OR list of strings
              Ex: "NVDA" or ["NVDA","AMD"]
        sample: str
            Sample length, required if "start" or "end" is missing
            Enter as number then frequency string (D, W, M, Y)
              Ex: "30d", "3m", "5y", etc.
        start: str
            Beginning date of sample, required if "end" or "sample" is missing
              Ex: '2020-01-01'
        end: str
            Ending date of sample, required if "start" or "sample" is missing
              Ex: '2022-05-01''
        intraday: bool
            True to return intraday data
            Default is 'False' to return end-of-day data
            See moabdb.com to look at subscriptions for intraday access
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


def get_treasuries(sample="1y",
                   start=None, end=None):
    """
    get_treasuries paramaters:
        sample: str
            Sample length, required if "start" or "end" is missing
            Enter as number then frequency string (D, W, M, Y)
              Ex: "30d", "3m", "5y", etc.
        start: str
            Beginning date of sample, required if "end" or "sample" is missing
              Ex: '2020-01-01'
        end: str
            Ending date of sample, required if "start" or "sample" is missing
              Ex: '2022-05-01''
    """

    # Check authorization
    if not _check_access():
        raise errors.MoabRequestError(
            "Premium datasets needs API credentials, see moabdb.com")

    # String time to integer time
    start_tm, end_tm = timewindows.get_unix_dates(sample, start, end)

    # Request treasury data
    columns = constants.TREASURY_COLUMNS
    return_db = _server_req("INTERNAL_TREASURY", start_tm, end_tm, "treasuries")
    return return_db[columns]
