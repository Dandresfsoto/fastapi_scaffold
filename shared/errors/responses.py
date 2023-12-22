from starlette import status

from shared.errors.models import ErrorDTO


BAD_REQUEST_ERROR = ErrorDTO(
    http_status=status.HTTP_400_BAD_REQUEST,
    code=status.HTTP_400_BAD_REQUEST,
    message='Bad Request',
)


SERVICE_UNAVAILABLE_ERROR = ErrorDTO(
    http_status=status.HTTP_503_SERVICE_UNAVAILABLE,
    code=status.HTTP_503_SERVICE_UNAVAILABLE,
    message='Service Unavailable',
)

SERVER_ERROR = ErrorDTO(
    http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message='Internal Server Error',
)
