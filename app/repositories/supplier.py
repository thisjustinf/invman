from sqlmodel.ext.asyncio.session import AsyncSession

from .base import BaseRepository
from ..models.supplier import Supplier, SupplierDTO
from ..models.mixins import AutoIncID


class SupplierRepository(BaseRepository[Supplier, AutoIncID, SupplierDTO]):
    """_summary_

    Args:
        BaseRepository (Supplier): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
