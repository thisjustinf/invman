from sqlmodel import Session
from uuid import UUID

from .base import BaseRepository
from ..models.inventory_item import InventoryItem


class InventoryItemRepository(BaseRepository[InventoryItem, UUID]):
    """_summary_

    Args:
        BaseRepository (InventoryItem): _description_
    """
    def __init__(self, session: Session):
        super().__init__(session)
