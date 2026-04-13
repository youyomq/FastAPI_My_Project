from src.models.records_oto_child import RecordsOTOChildOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTOChildDataMapper


class RecordsOTOChildRepository(BaseRepository):
    model = RecordsOTOChildOrm
    mapper = RecordOTOChildDataMapper