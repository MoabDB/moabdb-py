# MoabDB

import requests
from . import globals
from . import __version__


def hello():
    print("Welcome to Moab, where all data is exchanged!!")


def check_version() -> bool:
    """
    Checks the server's version, compairing the current version
    """
    res = requests.get(globals._dx_url + 'client_version/')
    return (res.text == __version__)
