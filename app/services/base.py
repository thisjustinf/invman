from typing import List
from uuid import UUID

from sqlmodel import SQLModel

from ..models.mixins import SKU, AutoIncID
from ..repositories.base import BaseRepository


class BaseService[T: SQLModel, U: (UUID, AutoIncID, SKU)]:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get_all(self) -> List[T]:
        return self.repository.get_all(T)

    def create(self, data: dict) -> None:
        return self.repository.create(T(**data))

    def update(self, id: U, data: dict) -> bool:
        self.repository.update(id, T(**data), T)

    def delete(self, id: U) -> bool:
        return self.repository.delete(id, T)
