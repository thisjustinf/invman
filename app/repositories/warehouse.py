from sqlmodel.ext.asyncio.session import AsyncSession

from .base import BaseRepository
from ..models.warehouse import Warehouse, WarehouseDTO
from ..models.mixins import AutoIncID


class WarehouseRepository(BaseRepository[Warehouse, AutoIncID, WarehouseDTO]):
    """_summary_

    Args:
        BaseRepository (Warehouse): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
