from fastapi import FastAPI

from health.services.health import HealthService
from health.views.health import register_health_view
from shared.errors.handlers import register_error_handlers


def new_app(health_service: HealthService) -> FastAPI:
    app = FastAPI()
    register_error_handlers(app)
    register_health_view(app, health_service)
    return app
