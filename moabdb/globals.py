# MoabDB

_api_key = ""
_api_username = ""
_dx_url = "https://api.moabdb.com/"
_daily_columns = ['symbol','date','close','open', 'high', 'low', 'volume']

#intra_columns = ['']

def login(username: str, key: str):
    """
    Logs in to the API to provide data that is not publically available
    :param key: The API key to use
    :return: None
    """

    global _api_key
    global _api_username

    _api_key = key
    _api_username = username


def set_dx_url(url: str):
    """
    Sets the URL for the MoabDB API
    Only useful for testing
    :param url: The URL to use
    :return: None
    """

    global _dx_url
    _dx_url = url
