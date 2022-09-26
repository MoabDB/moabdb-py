# Jackson Coxson

import base64
import io
import pandas as pd
import moabdx as mdx
from moabdx import protocol, body
import requests

bdy = body.DataRequest(body.DataType.Stocks,
                       "AAPL", False, 1325381285, 1577842085)

req = protocol.Reqres(1, protocol.Opcode.ReqFinData, bdy)
df = pd.read_parquet(io.BytesIO(req.send().body.data))
print(df)
