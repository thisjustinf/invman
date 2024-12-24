"""_summary_
"""

from sqlmodel import SQLModel, Relationship

# from .product_variant import ProductVariant
from .mixins import AutoIncrementIDMixin, TimestampMixin


class Product(
    AutoIncrementIDMixin,
    TimestampMixin,
    SQLModel,
    table=True
):
    __tablename__ = "products"

    name: str
    description: str
    category: str

    variants: list["ProductVariant"] = Relationship(back_populates="product")
