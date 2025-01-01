from sqlmodel import Session

from .base import BaseRepository
from ..models.purchase_order import PurchaseOrder


class PurchaseOrderRepository(BaseRepository[PurchaseOrder]):
    """_summary_

    Args:
        BaseRepository (PurchaseOrder): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
