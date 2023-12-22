from shared.errors.models import ErrorDTO


class ResponseException(Exception):
    def __init__(self, error: ErrorDTO):
        super().__init__(error.message)
        self.error = error
