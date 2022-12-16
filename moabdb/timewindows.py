"""Time window functions for MoabDB"""

import re
from datetime import datetime
import pandas as pd
from . import errors


def _to_unix_epoch(date_string):
    # Get uniq epoch time as integer
    unix_epoch = datetime.strptime(date_string, "%Y-%m-%d")
    t_m = (unix_epoch - datetime(1970, 1, 1)).total_seconds()
    return int(t_m)


def _to_unix_w_freq(sample_len, base_time, base_type):
    """
        Provide time frequency and base time,
            returns offset time.
        Enter negative end_tm as base_time to find start date.
        Enter positive beg_tm as base_time to find end date.
    """
    tm_freq, tm_unit = re.findall(r'(\d+)(\w+?)', sample_len)[0]
    tm_freq = int(tm_freq) * (-1) if base_type == 'End' else int(tm_freq)

    base_timestamp = pd.Timestamp(base_time, unit='s')

    if str.upper(tm_unit) == 'D':
        new_time = base_timestamp + pd.DateOffset(days=tm_freq)
    elif str.upper(tm_unit) == 'W':
        new_time = base_timestamp + pd.DateOffset(weeks=tm_freq)
    elif str.upper(tm_unit) == 'M':
        new_time = base_timestamp + pd.DateOffset(months=tm_freq)
    elif str.upper(tm_unit) == 'Y':
        new_time = base_timestamp + pd.DateOffset(years=tm_freq)
    else:
        raise errors.MoabRequestError("Unknown time unit, accepts: D, W, M, Y")
    return int(new_time.timestamp())


def get_unix_dates(sample_len: str, start_dt: str, end_dt: str):
    """
    Convert timestamps/samples into a start and end unix epoch time

    Args:
        sample_len (:obj:`str`, optional): The sample length to adjust the start/end by
        start_dt (:obj:`str`, optional): The start timestamp
        end_dt (:obj:`str`, optional): The end timestamp

    Returns:
        None: On success, this will return nothing

    Example::

        import moabdb as mdb
        mdb.login("your-signup-email@mail.com", "secret_key")
        print("Login succeeded")

    """
    # User provided sample length ...

    # ... but didn't provide anything else --> get recent sample
    if (end_dt is None) & (start_dt is None):
        today = datetime.now().strftime("%Y-%m-%d")
        end = _to_unix_epoch(today)
        start = _to_unix_w_freq(sample_len, end, 'End')

    # ... and provided start date --> find end date using sample length
    elif (end_dt is None) & (start_dt is not None):
        start = _to_unix_epoch(start_dt)
        end = _to_unix_w_freq(sample_len, start, 'Start')

    # ... and provided end date --> find start date using sample length
    elif (end_dt is not None) & (start_dt is None):
        end = _to_unix_epoch(end_dt)
        start = _to_unix_w_freq(sample_len, end, 'End')

    # ... and provided start and end date --> ignore sample length
    elif (end_dt is not None) & (start_dt is not None):
        end = _to_unix_epoch(end_dt)
        start = _to_unix_epoch(start_dt)

    # ... and provided something else --> error
    else:
        raise errors.MoabRequestError("Invalid date input")

    return (start, end)
