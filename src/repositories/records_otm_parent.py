from src.models.orders import RecordsOTMParentOrm
from src.repositories.mappers.mappers import RecordOTMParentDataMapper
from src.repositories.base import BaseRepository


class RecordsOTMParentRepository(BaseRepository):
    model = RecordsOTMParentOrm
    mapper = RecordOTMParentDataMapper