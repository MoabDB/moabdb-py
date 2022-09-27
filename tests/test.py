# Jackson Coxson

import io
import pandas as pd
from moabdx import protocol, body
from dateutil import parser

start = int(parser.parse("1970-01-01").timestamp())
end = int(parser.parse("2022-12-01").timestamp())
bdy = body.DataRequest(body.DataType.Stocks,
                       "aa", False, start, end)

req = protocol.Reqres(1, protocol.Opcode.ReqFinData, bdy)
df = pd.read_parquet(io.BytesIO(req.send().body.data))
print(df)
