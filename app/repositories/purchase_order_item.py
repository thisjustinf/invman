from sqlmodel.ext.asyncio.session import AsyncSession

from .base import BaseRepository
from ..models.purchase_order_item import PurchaseOrderItem, PurchaseOrderItemDTO
from ..models.mixins import AutoIncID


class PurchaseOrderItemRepository(
    BaseRepository[PurchaseOrderItem, AutoIncID, PurchaseOrderItemDTO]
):
    """_summary_

    Args:
        BaseRepository (PurchaseOrderItem): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
