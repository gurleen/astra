"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from astra import status_codes

class AstraException(Exception):
    status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR
    message: str

    def __init__(self, message: str = None):
        if message is not None:
            self.message = message


class NotFound(AstraException):
    status_code = status_codes.HTTP_404_NOT_FOUND
    message = "Resource not found"


class NotAuthorized(AstraException):
    status_code = status_codes.HTTP_401_UNAUTHORIZED
    message = "Not authorized"


class Forbidden(AstraException):
    status_codes = status_codes.HTTP_403_FORBIDDEN
    message = "Forbidden"


class MethodNotAllowed(AstraException):
    status_codes = status_codes.HTTP_405_METHOD_NOT_ALLOWED
    message = "Method Not Allowed"