class PageLimitError(Exception):
    def __init__(self, message, errors=[]):
        super().__init__(message)
        self.errors = errors

class OutOfRangeError(Exception):
    def __init__(self, message, errors=[]):
        super().__init__(message)
        self.errors = errors

class UnrecognizedResponseError(Exception):
    def __init__(self, message, errors=[]):
        super().__init__(message)
        self.errors = errors