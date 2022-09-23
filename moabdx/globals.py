# Jackson Coxson

_api_key = ""
_dx_url = "https://api.moabdx.com/"


def login(key: str):
    """
    Logs in to the API to provide data that is not publically available
    :param key: The API key to use
    :return: None
    """

    global _api_key
    _api_key = key


def set_dx_url(url: str):
    """
    Sets the URL for the MoabDX API
    Only useful for testing
    :param url: The URL to use
    :return: None
    """

    global _dx_url
    _dx_url = url
