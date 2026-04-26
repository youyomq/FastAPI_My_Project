from src.models.customers import CustomersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTMChildDataMapper


class RecordsOTMChildRepository(BaseRepository):
    model = CustomersOrm
    mapper = RecordOTMChildDataMapper
