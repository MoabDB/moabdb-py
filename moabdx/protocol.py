# Jackson Coxson

from typing import List
import base64


class Reqres:
    def __init__(self, version: int, op: int, body, auth: str = None):
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
        buffer.append(self.op)
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


class DataRequest:
    def __init__(self, data_type: int, ticker: str, intraday: bool, start: int, end: int):
        self.data_type = data_type
        self.ticker = ticker
        self.intraday = intraday
        self.start = start
        self.end = end

    def serialize(self) -> bytearray:
        buffer = bytearray([])
        buffer.append(self.data_type)
        buffer.append(len(self.ticker))
        buffer.extend(self.ticker.encode())
        if (self.intraday):
            buffer.append(1)
        else:
            buffer.append(0)
        buffer += self.start.to_bytes(4, 'little')
        buffer += self.end.to_bytes(4, 'little')
        return buffer
