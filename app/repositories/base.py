from typing import List
from uuid import UUID

from sqlmodel import Session, SQLModel, select, func


class BaseRepository[T: SQLModel, U: (UUID, int, str)]:
    def __init__(self, session: Session):
        self.session = session

    def create(self, item: T) -> None:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

    def get_one_by_id(self, id: U, entity: T) -> T | None:
        return self.session.get(entity, id)

    def delete(self, id: U, entity: T) -> bool:
        item = self.get_one_by_id(id, entity)
        if item:
            self.session.delete(item)
            self.session.commit()
            return True
        return False

    def get_all(self, entity: T) -> List[T]:
        return self.session.exec(select(entity)).all()

    def count(self, entity: T) -> int:
        return self.session.exec(
            select(func.count()).select_from(entity)
        ).scalar_one()
