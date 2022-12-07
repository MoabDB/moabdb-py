import re
import requests
from datetime import datetime

def convert_seconds(date_string):
    # Get UTC time as integer
    utc_time = datetime.strptime(date_string, "%Y-%m-%d")
    tm = (utc_time - datetime(1970, 1, 1)).total_seconds()
    return int(tm)   

def convert_seconds_w_freq(sample_len, base_time):
    """
        Provide time frequency and base time, 
            returns offset time.
        Enter negative end_tm as base_time to find start date.
        Enter positive beg_tm as base_time to find end date.
    """
    tm_freq = int(re.findall(r'(\d+)(\w+?)', sample_len)[0][0])
    tm_unit = str.upper(re.findall(r'(\d+)(\w+?)', sample_len)[0][1])    
    if tm_unit == 'D':
        new_time = base_time + (tm_freq * 86400)
    elif tm_unit == 'W':
        new_time = base_time + (tm_freq * 604800)                
    elif tm_unit == 'M':
        new_time = base_time + (tm_freq * 1900800)                
    elif tm_unit == 'Y':
        new_time = base_time + (tm_freq * 21772800)
    else:
        print("Unknown time unit, accepts: D, W, M, Y")
    if base_time < 0:
        new_time *= -1
    new_time_secs = convert_seconds(new_time)
    return(new_time_secs)


def get_sample_dts(sample_len, start_dt, end_dt):
    # User wants a sample window of a specific length and ending today
    if (sample_len is not None) & (end_dt is None) & (start_dt is None):
        today = datetime.now().strftime("%Y-%m-%d")
        end = convert_seconds(today)
        start = get_seconds_w_freq(sample_len, -end)

    # User wants a sample window of a specific length and starting on a specific date
    else if (sample_len is not None) & (end_dt is None) & (start_dt is not None):
        start = convert_seconds(start_dt)   
        end = get_seconds_w_freq(sample_len, start)

    # User wants a sample window of a specific length and ending on a specific date
    else if (sample_len is not None) & (end_dt is not None) & (start_dt is None):
        end = convert_seconds(end_dt)   
        start = get_seconds_w_freq(sample_len, -end)

    else if (sample_len is not None) & (end_dt is not None) & (start_dt is not None):
        print("Sample length, end date, and start date given ... ignoring sample length")
        end = convert_seconds(end_dt)
        start = convert_seconds(start_dt)

    # User wants a sample window between two specific dates
    else if (sample_len is None) & (end_dt is not None) & (start_dt is not None):
        end = convert_seconds(end_dt)
        start = convert_seconds(start_dt)    

    # User didn't provide start date
    else if (sample_len is None) & (end_dt is not None) & (start_dt is None):
        sample_len = '30d'
        end = convert_seconds(end_dt)   
        start = get_seconds_w_freq(sample_len, -end)

    # User didn't provide end date
    else if (sample_len is None) & (end_dt is None) & (start_dt is not None):
        sample_len = '30d'
        start = convert_seconds(start_dt)   
        end = get_seconds_w_freq(sample_len, start)

    return(start, end)