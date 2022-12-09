"""MoabDB API Library"""

import io
from base64 import b64encode, b64decode
import requests
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


def _send_request(request: proto_wrapper.REQUEST) -> proto_wrapper.RESPONSE:
    """
    Sends a request to the MoabDB API
    :param Request: The request to send
    :return: The response from the server
    """
    serialized_req = request.SerializeToString()
    headers = {
        'x-req': b64encode(serialized_req)
    }

    try:
        res = requests.get(constants.DB_URL + 'request/v1/',
                           headers=headers, timeout=180)

        if res.status_code == 502:
            raise errors.MoabInternalError("Take2 server is down")
        if res.status_code != 200:
            raise errors.MoabHttpError("Unknown error")

        res = proto_wrapper.RESPONSE().FromString(b64decode(res.text))
        return res

    except requests.exceptions.Timeout as exc:
        raise errors.MoabHttpError("Unable to connect to server") from exc


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

    res = _send_request(req)

    if res.code == 200:
        # Place data into a dataframe
        pq_file = io.BytesIO(res.data)
        try:
            d_f = pd.read_parquet(pq_file)
            return d_f
        except Exception as exc:
            raise errors.MoabResponseError(
                "Server returned invalid data") from exc
    elif res.code == 400:
        raise errors.MoabRequestError("Invalid request: " + res.message)
    elif res.code == 401:
        raise errors.MoabUnauthorizedError("Invalid credentials")
    elif res.code == 404:
        raise errors.MoabNotFoundError(res.message + " not found")
    elif res.code == 500:
        raise errors.MoabInternalError("Server error: " + res.message)
    else:
        raise errors.MoabResponseError(
            "Unknown error " + res.code + ": " + res.message)


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
        api_key: str
            api_key required for intraday data
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
        compile_tickers = []
        for tic in tickers:
            compile_tickers.append(_server_req(
                str.upper(tic), start_tm, end_tm, equity_freq))
        return_db = pd.concat(compile_tickers)[columns]
        return_db = return_db.set_index(columns[0:2]).unstack(0)

    # Unknown ticker request
    else:
        raise errors.MoabRequestError("Invalid window type")

    return return_db
