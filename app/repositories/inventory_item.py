from sqlmodel.ext.asyncio.session import AsyncSession
from uuid import UUID

from .base import BaseRepository
from ..models.inventory_item import InventoryItem, InventoryItemDTO


class InventoryItemRepository(BaseRepository[InventoryItem, UUID, InventoryItemDTO]):
    """_summary_

    Args:
        BaseRepository (InventoryItem): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, item):
        return await super().create(item)

    async def get_by_id(self, id: UUID) -> InventoryItem | None:
        return await super().get_one(InventoryItem.id == id)

    async def delete_by_id(self, id: UUID) -> bool:
        return await super().delete(InventoryItem.id == id)

    async def update(self, id: UUID, dto: InventoryItemDTO):
        await super().update(id, dto)
