from sqlmodel.ext.asyncio.session import AsyncSession
from app.repositories.inventory_item import InventoryItemRepository
import pytest_asyncio


@pytest_asyncio.fixture
async def inventory_item_repository(session: AsyncSession):
    return InventoryItemRepository(session)
