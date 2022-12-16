"""MoabDB Constants Manager"""

from . import proto_wrapper

API_KEY = ""
API_USERNAME = ""
DB_URL = "https://api.moabdb.com/"
DAILY_COLUMNS = ['symbol', 'date', 'close', 'open', 'high', 'low', 'volume']
INTRA_COLUMNS = ['symbol', 'time', 'price', 'bid', 'ask', 'volume']
TREASURY_COLUMNS = ['date', 'Treasury_1m', 'Treasury_2m', 'Treasury_3m',
                    'Treasury_4m', 'Treasury_6m', 'Treasury_1y', 'Treasury_2y',
                    'Treasury_3y', 'Treasury_5y', 'Treasury_7y', 'Treasury_10y',
                    'Treasury_20y', 'Treasury_30y', 'Realrate_5y', 'Realrate_7y',
                    'Realrate_10y', 'Realrate_20y', 'Realrate_30y']


def login(username: str, key: str):
    """
    Logs in to the API to provide data that is not publically available.
    Throws an error if the username/key is wrong, or if there's a connection error.

    Args:
        username (str): The email that you signed up with
        key (str): The key that you got at www.moabdb.com/account/member-api

    Returns:
        None: On success, this will return nothing

    Example::

        import moabdb as mdb
        mdb.login("your-signup-email@mail.com", "secret_key")
        print("Login succeeded")

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
