from datetime import datetime
from typing import TypeVar
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field

T = TypeVar("T")


class TimestampMixin(SQLModel):
    """Mixin for created_at and updated_at fields"""

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={
            "onupdate": datetime.utcnow}
    )


class AutoIncrementIDMixin(SQLModel):
    """Mixin for auto-incrementing integer primary keys"""

    id: int | None = Field(default=None, primary_key=True)


class UUIDMixin(SQLModel):
    """Mixin for UUID primary keys"""

    id: UUID = Field(default_factory=uuid4, primary_key=True)


class SKUMixin(SQLModel):
    """Mixin for SKU-based primary keys"""

    sku: str = Field(primary_key=True)


class SoftDeleteMixin(SQLModel):
    """Optional mixin for soft delete functionality"""

    is_active: bool = Field(default=True, index=True)
