"""MoabDB Constants"""

from . import proto_wrapper

API_KEY = ""
API_USERNAME = ""
DB_URL = "https://api.moabdb.com/"
DAILY_COLUMNS = ['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'VWAP',\
                 'BidPrc', 'AskPrc', 'Volume', 'Trades']
INTRA_COLUMNS = ['Symbol', 'Time', 'Trades', 'Volume', 'Imbalance','Close',\
                 'VWAP', 'BidPrc', 'AskPrc', 'BidSz', 'AskSz']
TREASURY_COLUMNS = ['date', 'Treasury_1m', 'Treasury_2m', 'Treasury_3m',
                    'Treasury_4m', 'Treasury_6m', 'Treasury_1y', 'Treasury_2y',
                    'Treasury_3y', 'Treasury_5y', 'Treasury_7y', 'Treasury_10y',
                    'Treasury_20y', 'Treasury_30y', 'Realrate_5y', 'Realrate_7y',
                    'Realrate_10y', 'Realrate_20y', 'Realrate_30y']


def login(username: str, key: str):
    """
    Logs in to the API to provide data that is not publically available
    :param key: The API key to use
    :return: None
    """

    # Create a login request
    req = proto_wrapper.REQUEST()
    req.token = key
    req.username = username

    res = req.send(DB_URL + 'login/v1/')

    res.throw()
    # pylint: disable=global-statement
    global API_KEY
    global API_USERNAME

    API_KEY = key
    API_USERNAME = username
