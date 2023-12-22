from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.app import new_app
from app.settings import AppSettings
from health.repositories.health import HealthRepository
from health.services.health import HealthService


app_settings = AppSettings()  # type: ignore

# Database session config
engine = create_async_engine(url=app_settings.database.dsn.unicode_string(), pool_size=app_settings.database.pool_size)
session_maker = async_sessionmaker(bind=engine)

# Register models
health_repository = HealthRepository(session_maker)
health_service = HealthService(health_repository)

# Start FastAPI application
app = new_app(health_service=health_service)
