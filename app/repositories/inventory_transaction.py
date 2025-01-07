from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID

from .base import BaseRepository
from ..models.inventory_transaction import InventoryTransaction, InventoryTransactionDTO


class InventoryTransactionRepository(
    BaseRepository[InventoryTransaction, UUID, InventoryTransactionDTO]
):
    """_summary_

    Args:
        BaseRepository (InventoryTransaction): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
