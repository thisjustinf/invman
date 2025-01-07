from sqlmodel.ext.asyncio.session import AsyncSession
from .base import BaseRepository
from ..models.product import Product, ProductDTO
from ..models.mixins import AutoIncID


class ProductRepository(BaseRepository[Product, AutoIncID, ProductDTO]):
    """_summary_

    Args:
        BaseRepository (Product): _description_
    """

    def __init__(self, session: AsyncSession):
        super().__init__(session)
