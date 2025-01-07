from sqlmodel import SQLModel, Relationship

from app.schemas.update import UpdateSchema
from .mixins import AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin


class WarehouseDTO(UpdateSchema):
    name: str
    address: str
    contact_info: str


class Warehouse(
    AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin, SQLModel, table=True
):
    __tablename__ = "warehouses"

    name: str
    address: str
    contact_info: str

    inventory_items: list["InventoryItem"] = Relationship(back_populates="warehouse")
