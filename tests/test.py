# Jackson Coxson

import moabdx as mdx
from moabdx import protocol
import requests

r = protocol.DataRequest(protocol.DataType.Stocks,
                         "APPL", False, 6969, 12345)
print(r.serialize())
p = protocol.DataRequest(raw_bytes=r.serialize())
print(p.serialize())
assert r == p
