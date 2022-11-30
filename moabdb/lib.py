# MoabDB

import requests
from . import globals
from . import __version__
from protocol import Request, Response


def hello():
    print("Welcome to Moab, where all data is exchanged!!")


def check_version() -> bool:
    """
    Checks the server's version, compairing the current version
    """
    res = requests.get(globals._dx_url + 'client_version/')
    return (res.text == __version__)


def send_request(request: Request) -> Response:
    """
    Sends a request to the MoabDB API
    :param Request: The request to send
    :return: The response from the server
    """
    res = requests.post(globals._dx_url + 'request/', data=Request)
    return res
