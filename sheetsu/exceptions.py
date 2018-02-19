class UnknownRequestMethod(Exception):
    """Exception raised once unexpected HTTP request code"""
    pass

class UnexpectedResponseCode(Exception):
    """Raised when unexpected HTTP response code is received"""
    pass
