"""MoabDB Constants"""
# MoabDB

API_KEY = ""
API_USERNAME = ""
DB_URL = "https://api.moabdb.com/"
DAILY_COLUMNS = ['symbol', 'date', 'close', 'open', 'high', 'low', 'volume']

#intra_columns = ['']


def login(username: str, key: str):
    """
    Logs in to the API to provide data that is not publically available
    :param key: The API key to use
    :return: None
    """

    # pylint: disable=global-statement
    global API_KEY
    global API_USERNAME

    API_KEY = key
    API_USERNAME = username
