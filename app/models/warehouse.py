from sqlmodel import SQLModel, Relationship
from .mixins import AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin
# from .inventory_item import InventoryItem


class Warehouse(
    AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin, SQLModel, table=True
):
    __tablename__ = "warehouses"

    name: str
    address: str
    contact_info: str

    inventory_items: list["InventoryItem"] = Relationship(
        back_populates="warehouse")
