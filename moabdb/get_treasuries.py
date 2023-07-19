#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# moabdb - Online finance database
# https://github.com/MoabDB
# https://moabdb.com
# Copyright 2022-2023
#

"""
The get_treasuries() function retrieves historical treasury data from the MoabDB API.
"""

from . import constants
from . import errors
from . import timewindows
from .lib import _check_access, _server_req
from .constants import pd


def get_treasuries(sample: str = "1y",
                   start: str = None,
                   end: str = None) -> pd.DataFrame:
    """
    Gets treasury data from the MoabDB API.

    Args:
        sample (str, optional): Sample length, required if "start" or "end" is missing.
        start (str, optional): Beginning date of sample, required if "end" or "sample" is missing.
        end (str, optional): Ending date of sample, required if "start" or "sample" is missing.

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response.
        errors.MoabRequestError: If the server has a problem interpreting the request,
            or if an invalid parameter is passed.
        errors.MoabInternalError: If the server runs into an unrecoverable error internally.
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response.
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype.
        errors.MoabNotFoundError: If the data requested wasn't found.
        errors.MoabUnknownError: If the error code couldn't be parsed.

    Returns:
        pandas.DataFrame: A DataFrame containing daily treasury data.
            Index: Date (datetime64): Date of the data point as YYYY-MM-DD.
            Columns:
                - Treasury_1m (float): Treasury yield for a 1-month maturity.
                - Treasury_2m (float): Treasury yield for a 2-month maturity.
                - Treasury_3m (float): Treasury yield for a 3-month maturity.
                - Treasury_4m (float): Treasury yield for a 4-month maturity.
                - Treasury_6m (float): Treasury yield for a 6-month maturity.
                - Treasury_1y (float): Treasury yield for a 1-year maturity.
                - Treasury_2y (float): Treasury yield for a 2-year maturity.
                - Treasury_3y (float): Treasury yield for a 3-year maturity.
                - Treasury_5y (float): Treasury yield for a 5-year maturity.
                - Treasury_7y (float): Treasury yield for a 7-year maturity.
                - Treasury_10y (float): Treasury yield for a 10-year maturity.
                - Treasury_20y (float): Treasury yield for a 20-year maturity.
                - Treasury_30y (float): Treasury yield for a 30-year maturity.
                - Realrate_5y (float): Real interest rate for a 5-year maturity.
                - Realrate_7y (float): Real interest rate for a 7-year maturity.
                - Realrate_10y (float): Real interest rate for a 10-year maturity.
                - Realrate_20y (float): Real interest rate for a 20-year maturity.
                - Realrate_30y (float): Real interest rate for a 30-year maturity.

    Examples:

        - Request the last year of treasury data:
            import moabdb as mdb
            df = mdb.get_treasuries("1y")

        - Request a specific month of data:
            import moabdb as mdb
            df = mdb.get_treasuries(start="2022-04-01", sample="1m")

        - Request treasury data for a specific date range:
            import moabdb as mdb
            df = mdb.get_treasuries(start="2020-01-01", end="2020-12-31")

    """

    # Check authorization
    if not _check_access():
        raise errors.MoabRequestError(
            "Premium datasets needs API credentials, see moabdb.com")

    # String time to integer time
    start_tm, end_tm = timewindows.get_unix_dates(sample, start, end)

    # Request treasury data
    columns = constants.TREASURY_COLUMNS
    return_db = _server_req("INTERNAL_TREASURY",
                            start_tm, end_tm, "treasuries")

    # Format treasury data
    return_db = return_db[columns].set_index(columns[0])

    return return_db
