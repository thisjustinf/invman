"""_summary_
"""

from pydantic import condecimal
from sqlmodel import Field, Relationship, SQLModel

from app.schemas.update import UpdateSchema

from .mixins import TimestampMixin, UUIDMixin


class InventoryItemDTO(UpdateSchema):
    quantity: int
    bin_location: str
    cost_price: condecimal(max_digits=10, decimal_places=2)


class InventoryItem(UUIDMixin, TimestampMixin, SQLModel, table=True):
    __tablename__ = "inventory_items"

    variant_sku: str = Field(foreign_key="product_variants.sku")
    warehouse_id: int = Field(foreign_key="warehouses.id")
    quantity: int
    bin_location: str
    cost_price: condecimal(max_digits=10, decimal_places=2)

    variant: "ProductVariant" = Relationship(back_populates="inventory_items")
    warehouse: "Warehouse" = Relationship(back_populates="inventory_items")
    transactions: list["InventoryTransaction"] = Relationship(
        back_populates="inventory_item"
    )
