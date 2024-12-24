from sqlmodel import SQLModel, Relationship
from .mixins import AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin
# from .purchase_order import PurchaseOrder


class Supplier(
    AutoIncrementIDMixin, TimestampMixin, SoftDeleteMixin, SQLModel, table=True
):
    __tablename__ = "suppliers"

    name: str
    contact_info: str

    purchase_orders: list["PurchaseOrder"] = Relationship(
        back_populates="supplier")
