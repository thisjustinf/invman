from sqlmodel import Session

from .base import BaseRepository
from ..models.purchase_order_item import PurchaseOrderItem
from ..models.mixins import AutoIncID


class PurchaseOrderItemRepository(
    BaseRepository[PurchaseOrderItem, AutoIncID]
):
    """_summary_

    Args:
        BaseRepository (PurchaseOrderItem): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
