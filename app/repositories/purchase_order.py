from sqlmodel.ext.asyncio.session import AsyncSession

from .base import BaseRepository
from ..models.purchase_order import PurchaseOrder, PurchaseOrderDTO
from ..models.mixins import AutoIncID


class PurchaseOrderRepository(
    BaseRepository[PurchaseOrder, AutoIncID, PurchaseOrderDTO]
):
    """_summary_

    Args:
        BaseRepository (PurchaseOrder): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
