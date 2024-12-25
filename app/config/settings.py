import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT: int | str = os.environ.get("POSTGRES_PORT")
    POSTGRES_NAME: str = os.environ.get("POSTGRES_NAME")
    ASYNC_DATABASE_URI: any | None = (
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{
            POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
    )

    model_config = SettingsConfigDict(env_file=f"../../env/.env.{ENVIRONMENT}")
