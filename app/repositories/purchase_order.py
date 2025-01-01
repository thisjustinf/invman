from sqlmodel import Session

from .base import BaseRepository
from ..models.purchase_order import PurchaseOrder
from ..models.mixins import AutoIncID


class PurchaseOrderRepository(BaseRepository[PurchaseOrder, AutoIncID]):
    """_summary_

    Args:
        BaseRepository (PurchaseOrder): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
