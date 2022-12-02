# MoabDB

import requests
from . import globals
from . import __version__
from . import protocol_pb2
from . import convert_seconds, get_seconds_w_freq, time_window

from base64 import b64encode, b64decode


def hello():
    print("Welcome to Moab, where all data is exchanged!!")


def check_version() -> bool:
    """
    Checks the server's version, compairing the current version
    """
    res = requests.get(globals._dx_url + 'client_version/')
    return (res.text == __version__)


def send_request(request: protocol_pb2.Request) -> protocol_pb2.Response:
    """
    Sends a request to the MoabDB API
    :param Request: The request to send
    :return: The response from the server
    """
    s = request.SerializeToString()
    headers = {
        'x-req': b64encode(s)
    }
    res = requests.get(globals._dx_url + 'request/v1/', headers=headers)
    res = protocol_pb2.Response().FromString(b64decode(res.text))
    return res


def server_req(ticker, start, end, datatype):
    # Request data from moabdb server
    req = protocol_pb2.Request()
    req.symbol = ticker
    req.start = start
    req.end = end
    req.datatype = datatype

    res = send_request(req)

    if res.code == 200:
        # Place data into a dataframe
        pq_file = io.BytesIO(res.data)
        df = pd.read_parquet(pq_file)
        return(df)
    else:
        print(res.code)
        print(res.message)


def get_equity(tickers, sample="5d", 
            start=None, end=None,
            intraday=False, api_key=None):
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
    if (intraday == True):
        is_authorized = _check_access(api_key)
        equity_freq = "intraday_stocks"
        if is_authorized == 0:
            print("Error: Subscription required to access intraday data")
            intraday = False
            equity_freq = "daily_stocks"

    # String time to integer timne
    start_tm, end_tm = _request_window(sample_len, start, end)

    # Single ticker request 
    if isinstance(tickers, str):
        return_db = _server_req(str.upper(tickers), start_tm, end_tm, equity_freq)

    # List of tickers request
    else if isinstance(tickers, list):
        compile_tickers = []
        for tic in tickers:
            compile_tickers.append(_server_req(str.upper(tic), start_tm, end_tm, equity_freq))
        return_db = pd.concat(compile_tickers)
        return_db = return_db.set_index(['Ticker','Date']).unstack(0)

    # Unknown ticker request
    else:
        print("Error accessing tickers: Enter ticker or list of tickers")

    return(return_db)

