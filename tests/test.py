# Jackson Coxson

import moabdx as mdx
from moabdx import protocol

r = protocol.Reqres(1, 4, [1, 2, 3, 4], auth="yarhar")
b6 = r.serialize()
print(b6)
