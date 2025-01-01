from sqlmodel import Session

from .base import BaseRepository
from ..models.product_variant import ProductVariant


class ProductVariantRepository(BaseRepository[ProductVariant]):
    """_summary_

    Args:
        BaseRepository (ProductVariant): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
