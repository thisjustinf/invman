from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from .mixins import UUIDMixin


class InventoryTransaction(UUIDMixin, SQLModel, table=True):
    __tablename__ = "inventory_transactions"

    item_id: UUID = Field(foreign_key="inventory_items.id")
    type: str
    quantity: int
    reference_number: str
    transaction_data: dict = Field(sa_column=Column(JSON))
    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )  # Only needs created_at

    inventory_item: "InventoryItem" = Relationship(back_populates="transactions")
