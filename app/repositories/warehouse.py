from sqlmodel import Session

from .base import BaseRepository
from ..models.warehouse import Warehouse


class WarehouseRepository(BaseRepository[Warehouse]):
    """_summary_

    Args:
        BaseRepository (Warehouse): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
