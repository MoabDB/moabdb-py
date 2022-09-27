# Jackson Coxson

from enum import Enum
from .errors import RequestError, InternalError


class DataType(Enum):
    Stocks = 0
    Options = 1


class DataRequest:
    def __init__(self, data_type: DataType = None, ticker: str = None, intraday: bool = False, start: int = None, end: int = None, raw_bytes: bytearray = None, op=None):
        if raw_bytes is not None:
            # Ensure the decoded bytes is long enough
            if len(raw_bytes) < 11:
                raise Exception(RequestError.InvalidBody)

            self.data_type = DataType(raw_bytes[0])
            ticker_len = raw_bytes[1]

            # Ensure the decoded bytes is long enough
            if len(raw_bytes) < 11 + ticker_len:
                raise Exception(RequestError.InvalidBody)

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
            raise Exception(RequestError.InvalidBody)

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
        buffer += int(self.start).to_bytes(4, 'little')
        buffer += int(self.end).to_bytes(4, 'little')
        return buffer


class DataResponse:
    def __init__(self, success: bool = True, data: bytearray = None, raw_bytes: bytearray = None, op=None):
        if raw_bytes is not None:
            if len(raw_bytes) < 2:
                raise Exception(RequestError.InvalidBody)

            if raw_bytes[0] == 0:
                self.success = False
            else:
                self.success = True

            self.data = raw_bytes[1:]
            return

        if data is None:
            raise Exception(RequestError.InvalidBody)

        self.data = data
        self.success = success