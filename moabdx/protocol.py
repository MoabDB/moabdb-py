# Jackson Coxson
from __future__ import annotations

from typing import List
from enum import Enum

from . import body
from . import globals

import base64
import requests


class Opcode(Enum):
    ReqEpochTime = 0x0
    ResEpochTime = 0x1
    EndConnection = 0x2
    ClientPubKey = 0x3
    ReqFinData = 0x4
    ResFinData = 0x5


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
                raise Exception(RequestError.InvalidHeader)

            packet_size = int.from_bytes(raw_bytes[0:4], 'little')
            if len(raw_bytes) < packet_size:
                raise Exception(RequestError.InvalidHeader)

            self.version = raw_bytes[4]

            raw_opcode = raw_bytes[5]

            try:
                e = InternalError(raw_opcode)
                raise Exception(e)
            except:
                pass

            try:
                e = RequestError(raw_opcode)
                raise Exception(e)
            except:
                pass

            try:
                self.op = Opcode(raw_bytes[5])
            except (ValueError):
                raise Exception(Opcode.UnknownError)

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
            raise Exception(RequestError.InvalidHeader)

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
        response = requests.get(
            globals._dx_url + 'request/', headers={'x-req': s})
        if response.status_code != 200:
            raise Exception(RequestError.UnknownError)
        decoded = base64.b64decode(response.text)
        return (Reqres(raw_bytes=decoded))
