from src.models.licenses import LicensesOrm
from src.repositories.base import BaseRepository


class LicensesRepository(BaseRepository):
    model = LicensesOrm