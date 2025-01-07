from sqlmodel import SQLModel, Relationship

from app.schemas.update import UpdateSchema
from .mixins import AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin


class SupplierDTO(UpdateSchema):
    name: str
    contact_info: str


class Supplier(
    AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin, SQLModel, table=True
):
    __tablename__ = "suppliers"

    name: str
    contact_info: str

    purchase_orders: list["PurchaseOrder"] = Relationship(back_populates="supplier")
