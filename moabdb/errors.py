"""MoabDB Errors"""


class MoabError(Exception):
    """Base class for exceptions in this module."""


class MoabRequestError(MoabError):
    """Exception raised for problems with interpreting the request.
        Thrown if bad parameters are passed or if the server recieves a poorly crafted request.

    Args:
        message (str): The message that was returned with the request error

    Attributes:
        message (str): The message that was returned with the request error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabInternalError(MoabError):
    """Exception raised for an internal error that occured on the server outside of user control.
        A user should not be able to reliably throw this.

    Args:
        message (str): The message that was returned with the internal error

    Attributes:
        message (str): The message that was returned with the internal error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabResponseError(MoabError):
    """Exception raised for problems interpreting the response

    Args:
        message (str): The message that was returned with the response error

    Attributes:
        message (str): The message that was returned with the response error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabHttpError(MoabError):
    """Exception raised for an error transporting the payload.
        This will be thrown if the client cannot reach the server's HTTP endpoint,
        or if the endpoint responds outside of HTTP's RFC.

    Args:
        message (str): The message that was returned with the HTTP error

    Attributes:
        message (str): The message that was returned with the HTTP error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabUnauthorizedError(MoabError):
    """Exception raised when the client is not authorized to request desired data.

    Args:
        message (str): The message that was returned with the error

    Attributes:
        message (str): The message that was returned with the error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabNotFoundError(MoabError):
    """Exception raised when the server cannot find the requested data.

    Args:
        message (str): The message that was returned with the error

    Attributes:
        message (str): The message that was returned with the error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MoabUnknownError(MoabError):
    """Exception raised when the server returns an unknown error code

    Args:
        message (str): The message that was returned with the error

    Attributes:
        message (str): The message that was returned with the error
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
