import re
import requests
from pandas import DateOffset
from datetime import datetime

def to_unix_epoch(date_string):
    # Get uniq epoch time as integer
    unix_epoch = datetime.strptime(date_string, "%Y-%m-%d")
    tm = (unix_epoch - datetime(1970, 1, 1)).total_seconds()
    return int(tm)   

def to_unix_w_freq(sample_len, base_time, base_type):
    """
        Provide time frequency and base time, 
            returns offset time.
        Enter negative end_tm as base_time to find start date.
        Enter positive beg_tm as base_time to find end date.
    """
    tm_freq, tm_unit = re.findall(r'(\d+)(\w+?)', sample_len)[0]
    tm_freq = int(tm_freq) *(-1) if base_type == 'End' else int(tm_freq)

    base_timestamp = pd.Timestamp(base_time, unit='s')

    if str.upper(tm_unit) == 'D':
        new_time = base_timestamp + DateOffset(days=tm_freq)
    elif str.upper(tm_unit) == 'W':
        new_time = base_timestamp + DateOffset(weeks=tm_freq)
    elif str.upper(tm_unit) == 'M':
        new_time = base_timestamp + DateOffset(months=tm_freq)
    elif str.upper(tm_unit) == 'Y':
        new_time = base_timestamp + DateOffset(years=tm_freq)
    else:
        print("Unknown time unit, accepts: D, W, M, Y")
    return(new_time.timestamp())

def get_sample_dates(sample_len, start_dt, end_dt):
    # User provided sample length ...

    # ... but didn't provide anything else --> get recent sample
    if (end_dt is None) & (start_dt is None):
        today = datetime.now().strftime("%Y-%m-%d")
        end = to_unix_epoch(today)
        start = to_unix_w_freq(sample_len, end, 'End')

    # ... and provided start date --> find end date using sample length
    elif (end_dt is None) & (start_dt is not None):
        start = to_unix_epoch(start_dt)   
        end = to_unix_w_freq(sample_len, start, 'Start')

    # ... and provided end date --> find start date using sample length
    elif (end_dt is not None) & (start_dt is None):
        end = to_unix_epoch(end_dt)   
        start = to_unix_w_freq(sample_len, end, 'End')

    # ... and provided start and end date --> ignore sample length
    elif (end_dt is not None) & (start_dt is not None):
        end = to_unix_epoch(end_dt)
        start = to_unix_epoch(start_dt)

    return(start, end)