# Jackson Coxson

import moabdx as mdx
from moabdx import protocol
import requests

r = protocol.Reqres(1, 4, protocol.DataRequest(
    1, "TSLA", False, 0, 12345)).serialize()

print(r)

res = requests.get(mdx.globals._dx_url + 'request/', headers={'x-req': r})
print(res.text)
