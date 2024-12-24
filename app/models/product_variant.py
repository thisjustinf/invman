from sqlmodel import SQLModel, Field, Column, JSON, Relationship
from pydantic import condecimal

# from app.models.inventory_item import InventoryItem


from .mixins import SKUMixin, TimestampMixin


class ProductVariant(SKUMixin, TimestampMixin, SQLModel, table=True):
    __tablename__ = "product_variants"

    product_id: int = Field(foreign_key="products.id")
    attributes: dict = Field(sa_column=Column(JSON))
    price: condecimal(max_digits=10, decimal_places=2)

    product: "Product" = Relationship(back_populates="variants")
    inventory_items: list["InventoryItem"] = Relationship(
        back_populates="variant")
