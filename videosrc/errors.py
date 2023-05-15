
class AuthenticationError(Exception):
    pass


class OptionError(Exception):
    pass


class MissingOptionError(OptionError):
    pass


class InvalidOptionError(OptionError):
    pass
