from os import environ

from sqlalchemy.engine import URL


def create_pg_url(
    drivername: str,
    username: str,
    password: str,
    host: str,
    port: int,
    database: str
) -> URL:
    return URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def create_pg_url_from_env() -> URL:
    return create_pg_url(
        drivername=environ.get("POSTGRES_DRIVERNAME", "postgresql+asyncpg"),
        username=environ.get("POSTGRES_USER"),
        password=environ.get("POSTGRES_PASSWORD"),
        host=environ.get("POSTGRES_HOST", "localhost"),
        port=environ.get("POSTGRES_PORT", "5432"),
        database=environ.get("POSTGRES_DB", "postgres"),
    )
