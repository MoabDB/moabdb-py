# MoabDB

import requests
from . import globals
from . import __version__
from . import protocol_pb2
from base64 import b64encode


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
