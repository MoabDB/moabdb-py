# Jackson Coxson

from typing import List
from enum import Enum
import base64


class Opcode(Enum):
    # opcodes
    ReqEpochTime = 0
    ResEpochTime = 1
    EndConnection = 2
    ClientPubKey = 3
    ReqFinData = 4
    ResFinData = 5

    # request errors
    InvalidBase64 = 50
    InvalidHeader = 51
    BadAuth = 52
    InvalidBody = 53


class Reqres:
    def __init__(self, version: int, op: Opcode, body, auth: str = None):
        """
        Initializes a request/response packet
        """
        self.version = version
        self.op = op
        self.body = body
        self.auth = auth

    def serialize(self) -> str:
        buffer = bytearray([])
        buffer.append(self.version)
        buffer.append(self.op.value)
        if self.auth is None:
            buffer.append(0)
        else:
            buffer.append(1)
            buffer.extend(self.auth.encode())
        buffer += self.body.serialize()

        buf_len = len(buffer).to_bytes(4, 'little')
        buf_len = bytearray(buf_len)
        buf_len += buffer

        pls = base64.b64encode(buf_len)
        return pls.decode('ascii')


class DataType(Enum):
    Stocks = 0
    Options = 1


class DataRequest:
    def __init__(self, data_type: DataType = None, ticker: str = None, intraday: bool = False, start: int = None, end: int = None, raw_bytes: bytearray = None):
        if raw_bytes is not None:
            # Ensure the decoded bytes is long enough
            if len(raw_bytes) < 11:
                raise Exception("Not enough bytes")

            self.data_type = DataType(raw_bytes[0])
            ticker_len = raw_bytes[1]

            # Ensure the decoded bytes is long enough
            if len(raw_bytes) < 11 + ticker_len:
                raise Exception("Not enough bytes")

            # Convert ticker bytes to string
            ticker_bytes = raw_bytes[2:(2 + ticker_len)]
            self.ticker = ticker_bytes.decode('ascii')

            # Convert intraday to bool
            intraday = raw_bytes[2 + ticker_len]
            if intraday == 0:
                self.intraday = False
            else:
                self.intraday = True

            # Get the start bytes
            start_bytes = raw_bytes[(3 + ticker_len):(7 + ticker_len)]
            self.start = int.from_bytes(start_bytes, 'little')

            # Get the end bytes
            end_bytes = raw_bytes[(7 + ticker_len):(11 + ticker_len)]
            self.end = int.from_bytes(end_bytes, 'little')

            return

        if data_type is None or ticker is None or start is None or end is None:
            raise Exception("Provide required arguments")

        self.data_type = data_type
        self.ticker = ticker
        self.intraday = intraday
        self.start = start
        self.end = end

    def serialize(self) -> bytearray:
        buffer = bytearray([])
        buffer.append(self.data_type.value)
        buffer.append(len(self.ticker))
        buffer.extend(self.ticker.encode())
        if (self.intraday):
            buffer.append(1)
        else:
            buffer.append(0)
        buffer += self.start.to_bytes(4, 'little')
        buffer += self.end.to_bytes(4, 'little')
        return buffer
