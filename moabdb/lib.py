"""MoabDB API Library"""

from . import constants
from . import proto_wrapper
from . import errors
from .constants import pd, io

def _check_access() -> bool:
    """
    Checks if the user has set the global credentials.
    This function is just a local sanity check, the server will
    check the credentials again.

    Returns:
        bool: True if the user has logged in
    """
    return not (constants.API_KEY == "" or constants.API_USERNAME == "")


def _server_req(ticker, start, end, datatype) -> pd.DataFrame:
    """
    Creates a high level request and parses the response

    Args:
        ticker (str): The ticker to query from the database
        start (int): The unix epoch time to start the query from
        end (int): The unix epoch time to stop searching at
        datatype (str): The data type that's being requested

    Raises:
        errors.MoabResponseError: If there's a problem interpreting the response
        errors.MoabRequestError: If the server has a problem interpreting the request
        errors.MoabInternalError: If the server runs into an unrecoverable error internally
        errors.MoabHttpError: If there's a problem transporting the payload or receiving a response
        errors.MoabUnauthorizedError: If the user is not authorized to request the datatype
        errors.MoabNotFoundError: If the data requested wasn't found
        errors.MoabUnknownError: If the error code couldn't be parsed

    Returns:
        pandas.DataFrame: A DataFrame containing the returned data.

    """
    # Request data from moabdb server
    req = proto_wrapper.REQUEST()
    req.symbol = ticker
    req.start = start
    req.end = end
    req.datatype = datatype

    if constants.API_KEY != "":
        req.token = constants.API_KEY
        req.username = constants.API_USERNAME

    res = req.send(constants.DB_URL + 'request/v1/')

    res.throw()

    # Place data into a dataframe
    pq_file = io.BytesIO(res.data)
    try:
        d_f = pd.read_parquet(pq_file)
        return d_f
    except Exception as exc:
        raise errors.MoabResponseError("Server returned invalid data") from exc
