from src.models.licenses import LicensesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import LicenseDataMapper


class LicensesRepository(BaseRepository):
    model = LicensesOrm
    mapper = LicenseDataMapper