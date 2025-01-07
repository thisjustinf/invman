from datetime import date
from pydantic import condecimal
from sqlmodel import SQLModel, Field, Relationship

from app.schemas.update import UpdateSchema
from .mixins import AutoIncrementIDMixin, TimestampMixin


class PurchaseOrderDTO(UpdateSchema):
    status: str
    expected_delivery_date: date
    total_amount: condecimal(max_digits=10, decimal_places=2)


class PurchaseOrder(AutoIncrementIDMixin, TimestampMixin, SQLModel, table=True):
    __tablename__ = "purchase_orders"

    supplier_id: int = Field(foreign_key="suppliers.id")
    status: str
    expected_delivery: date
    total_amount: condecimal(max_digits=10, decimal_places=2)

    supplier: "Supplier" = Relationship(back_populates="purchase_orders")
    items: list["PurchaseOrderItem"] = Relationship(back_populates="purchase_order")
