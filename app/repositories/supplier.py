from sqlmodel import Session

from .base import BaseRepository
from ..models.supplier import Supplier
from ..models.mixins import AutoIncID


class SupplierRepository(BaseRepository[Supplier, AutoIncID]):
    """_summary_

    Args:
        BaseRepository (Supplier): _description_
    """

    def __init__(self, session: Session):
        super().__init__(session)
