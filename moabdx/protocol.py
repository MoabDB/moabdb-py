# Jackson Coxson

from typing import List
from enum import Enum

from . import body
from . import globals
from __future__ import annotations

import base64
import requests


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


OpcodeDeserializers = {
    Opcode.ReqFinData: body.DataRequest,
    Opcode.ResFinData: body.DataResponse,
}


class Reqres:
    def __init__(self, version: int = None, op: Opcode = None, body=None, auth: str = None, raw_bytes: bytearray = None):
        """
        Initializes a request/response packet
        """

        if raw_bytes is not None:
            # Ensure that we have at least 7 bytes
            if len(raw_bytes) < 7:
                raise Exception("Not enough bytes")

            packet_size = int.from_bytes(raw_bytes[0:4], 'little')
            if len(raw_bytes) < packet_size:
                raise Exception("Not enough bytes")

            self.version = raw_bytes[4]
            self.op = Opcode(raw_bytes[5])

            body_bytes: bytearray = None

            if raw_bytes[6] == 0:
                self.auth = None
                body_bytes = raw_bytes[7:]
            else:
                self.auth = raw_bytes[7:39].decode('ascii')
                body_bytes = raw_bytes[40:]

            serializer = OpcodeDeserializers.get(self.op)
            if serializer is None:
                self.body = None
            else:
                self.body = serializer(raw_bytes=body_bytes, op=1)

            return

        if version is None or op is None or body is None:
            raise Exception("Pass enough arguments")

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

    def send(self) -> Reqres:
        s = self.serialize()
        response = requests.get(globals._dx_url, headers={'x-req': s})
        if response.status_code != 200:
            raise Exception("Non-200 error code")
        decoded = base64.b64decode(response.text)
        return (Reqres(raw_bytes=decoded))
