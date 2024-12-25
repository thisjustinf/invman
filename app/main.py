"""_summary_

Returns:
    _type_: _description_
"""

from contextlib import asynccontextmanager
from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database.db import create_db_and_tables
from .config.settings import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app: FastAPI = FastAPI(
    title="invman: Inventory Management API", lifespan=lifespan)


app.add_middleware(CORSMiddleware)


@app.get("/")
async def root() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    return {"message": "Hello World"}
