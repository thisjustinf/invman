from sqlmodel.ext.asyncio.session import AsyncSession

from .base import BaseRepository
from ..models.product_variant import ProductVariant, ProductVariantDTO
from ..models.mixins import SKU


class ProductVariantRepository(BaseRepository[ProductVariant, SKU, ProductVariantDTO]):
    """_summary_

    Args:
        BaseRepository (ProductVariant): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
