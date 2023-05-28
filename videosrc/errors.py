
class AuthenticationError(Exception):
    pass


class OptionError(Exception):
    pass


class MissingOptionError(OptionError):
    pass


class InvalidOptionError(OptionError):
    pass


class InvalidURLError(InvalidOptionError):
    pass


class StateReached(Exception):
    def __init__(self):
        super().__init__('State reached')
