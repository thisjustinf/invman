from sqlmodel import Session

from .base import BaseRepository
from ..models.product import Product


class ProductRepository(BaseRepository[Product]):
    """_summary_

    Args:
        BaseRepository (Product): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
