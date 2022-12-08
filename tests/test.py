# Jackson Coxson

from moabdb import get_equity
import pandas as pd
import io

for i in range(1, 100):
    print(get_equity("AAPL", "5y"))
