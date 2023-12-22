from fastapi import FastAPI, status

from health.services.health import HealthService
from health.views.models import HealthDTO
from shared.errors.exceptions import ResponseException
from shared.errors.responses import SERVICE_UNAVAILABLE_ERROR


def register_health_view(app: FastAPI, service: HealthService) -> None:
    @app.get(
        '/health',
        status_code=status.HTTP_200_OK,
        summary='Check if the service is healthy',
        response_description='A success message if the service is up. An error if not',
        tags=['Health']
    )
    async def health() -> HealthDTO:
        """
        Check if the service and it's dependencies are up
        """
        try:
            await service.check_service_is_up()
        except Exception as e:
            raise ResponseException(SERVICE_UNAVAILABLE_ERROR) from e

        return HealthDTO(message='Service is up!')
