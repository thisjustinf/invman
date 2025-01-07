"""_summary_
"""

from sqlmodel import SQLModel, Relationship

from app.schemas.update import UpdateSchema

from .mixins import AutoIncrementIDMixin, TimestampMixin


class ProductDTO(UpdateSchema):
    name: str
    description: str
    category: str


class Product(AutoIncrementIDMixin, TimestampMixin, SQLModel, table=True):
    __tablename__ = "products"

    name: str
    description: str
    category: str

    variants: list["ProductVariant"] = Relationship(back_populates="product")
