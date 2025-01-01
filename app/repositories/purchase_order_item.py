from sqlmodel import Session

from .base import BaseRepository
from ..models.purchase_order_item import PurchaseOrderItem


class PurchaseOrderItemRepository(BaseRepository[PurchaseOrderItem]):
    """_summary_

    Args:
        BaseRepository (PurchaseOrderItem): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
