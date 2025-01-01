from sqlmodel import Session
from uuid import UUID

from .base import BaseRepository
from ..models.inventory_transaction import InventoryTransaction


class InventoryTransactionRepository(
    BaseRepository[InventoryTransaction, UUID]
):
    """_summary_

    Args:
        BaseRepository (InventoryTransaction): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
