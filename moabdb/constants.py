"""MoabDB Constants"""

from . import proto_wrapper

API_KEY = ""
API_USERNAME = ""
DB_URL = "https://api.moabdb.com/"
DAILY_COLUMNS = ['symbol', 'date', 'close', 'open', 'high', 'low', 'volume']
INTRA_COLUMNS = ['symbol', 'time', 'price', 'bid', 'ask', 'volume']


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
