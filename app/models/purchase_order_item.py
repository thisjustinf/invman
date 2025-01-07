from sqlmodel import SQLModel, Field, Relationship

from app.schemas.update import UpdateSchema
from .mixins import AutoIncrementIDMixin, TimestampMixin


class PurchaseOrderItemDTO(UpdateSchema):
    quantity: int
    unit_price: condecimal(max_digits=10, decimal_places=2)


class PurchaseOrderItem(AutoIncrementIDMixin, TimestampMixin, SQLModel, table=True):
    __tablename__ = "purchase_order_items"

    po_id: int = Field(foreign_key="purchase_orders.id")
    variant_sku: str = Field(foreign_key="product_variants.sku")
    quantity: int
    unit_price: condecimal(max_digits=10, decimal_places=2)

    purchase_order: "PurchaseOrder" = Relationship(back_populates="items")
    variant: "ProductVariant" = Relationship()
