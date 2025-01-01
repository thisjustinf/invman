from sqlmodel import Session

from .base import BaseRepository
from ..models.inventory_transaction import InventoryTransaction


class InventoryTransactionRepository(BaseRepository[InventoryTransaction]):
    """_summary_

    Args:
        BaseRepository (InventoryTransaction): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
