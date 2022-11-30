# Jackson Coxson

from moabdb import protocol_pb2, send_request, check_version
import pandas as pd
import io

print(check_version())

for i in range(1, 100):
    req = protocol_pb2.Request()
    req.symbol = "AAPL"
    req.start = 1543554489
    req.end = 1548825309
    req.datatype = "intraday_stocks"

    res = send_request(req)

    if res.code == 200:
        # Slap the data into a pandas dataframe
        pq_file = io.BytesIO(res.data)
        df = pd.read_parquet(pq_file)
        print(df)
    else:
        print(res.code)
        print(res.message)
