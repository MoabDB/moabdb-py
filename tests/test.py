# Jackson Coxson

import base64
import moabdx as mdx
from moabdx import protocol, body
import requests

bdy = body.DataRequest(body.DataType.Stocks,
                       "APPL", False, 6969, 12345)

req = protocol.Reqres(1, protocol.Opcode.ReqFinData, bdy)

s_req = req.serialize()
bs_req = base64.b64decode(s_req)

parsed = protocol.Reqres(raw_bytes=bs_req)

assert parsed.serialize() == s_req
