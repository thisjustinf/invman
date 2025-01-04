import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT")
    POSTGRES_DRIVERNAME: str = os.environ.get("POSTGRES_DRIVERNAME")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT: int | str = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    ASYNC_DATABASE_URI: str = (
        f"{POSTGRES_DRIVERNAME}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{
            POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    model_config = SettingsConfigDict(env_file=f"../../.env.{ENVIRONMENT}")
