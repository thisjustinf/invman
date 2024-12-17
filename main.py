"""_summary_

Returns:
    _type_: _description_
"""
from fastapi import FastAPI

app: FastAPI = FastAPI(title="invman: Inventory Management API")


@app.get("/")
async def root() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    return {"message": "Hello World"}
