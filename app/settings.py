from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):  # type: ignore
    dsn: PostgresDsn
    pool_size: int


class CorsSettings(BaseSettings):  # type: ignore
    whitelist: str


class AppSettings(BaseSettings):  # type: ignore
    app_name: str
    database: DatabaseSettings
    cors_origin: CorsSettings

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'
        extra = 'ignore'
