from sqlmodel import Session

from .base import BaseRepository
from ..models.warehouse import Warehouse
from ..models.mixins import AutoIncID


class WarehouseRepository(BaseRepository[Warehouse, AutoIncID]):
    """_summary_

    Args:
        BaseRepository (Warehouse): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
