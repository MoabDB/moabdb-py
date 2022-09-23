# Jackson Coxson

from typing import List
import base64


class Reqres:
    def __init__(self, version: int, op: int, body: List, auth: str = None):
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
        buffer.extend(self.body)
        pls = base64.b64encode(buffer)
        return pls.decode('ascii')
