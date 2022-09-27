# Jackson Coxson

from enum import Enum


class InternalError(Enum):
    Unimplmented = 0x30
    CompressData = 0x31
    DatabaseConnection = 0x32
    UnknownError = 0x4f


class RequestError(Enum):
    InvalidBase64 = 0x50
    InvalidHeader = 0x51
    BadAuth = 0x52
    InvalidBody = 0x53
    UnknownError = 0x6f
