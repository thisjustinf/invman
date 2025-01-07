from typing import List, TypeVar
from uuid import UUID

from sqlalchemy import ColumnExpressionArgument
from sqlmodel import SQLModel, func, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.update import UpdateSchema

from ..models.mixins import SKU, AutoIncID

T = TypeVar("T", bound=SQLModel, infer_variance=True)
U = TypeVar("U", UUID, AutoIncID, SKU)
V = TypeVar("V", bound=UpdateSchema)
type Query = ColumnExpressionArgument[bool] | bool


class BaseRepository[T, U, V]:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, item: T) -> None:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)

    async def get_one(self, search_criteria: Query) -> T | None:
        result = await self.session.exec(select(T).where(search_criteria))
        return result.first()

    async def delete(self, search_criteria: Query) -> bool:
        item: T | None = await self.get_one(search_criteria)
        if item:
            await self.session.delete(item)
            await self.session.commit()
            return True
        return False

    async def get_all(self) -> List[T]:
        return await self.session.exec(select(T)).all()

    async def count(self, entity: T) -> int:
        return await self.session.exec(select(func.count()).select_from(T))

    async def update(self, search_criteria: Query, dto: V) -> None:
        item = await self.get_one(search_criteria)
        if item:
            fields: List[str] = list(dto.__dict__.keys())
            for f in fields:
                item
            self.session.add(item)
            await self.session.commit()
            await self.session.refresh(item)
