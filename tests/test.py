# Jackson Coxson

import io
import pandas as pd
from moabdx import protocol, body
from dateutil import parser

start = int(parser.parse("2012-01-01").timestamp())
end = int(parser.parse("2020-01-01").timestamp())
bdy = body.DataRequest(body.DataType.Stocks,
                       "gme", False, start, end)

req = protocol.Reqres(1, protocol.Opcode.ReqFinData, bdy)
df = pd.read_parquet(io.BytesIO(req.send().body.data))
print(df)
