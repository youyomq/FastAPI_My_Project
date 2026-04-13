from src.models.records_otm_child import RecordsOTMChildOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTMChildDataMapper


class RecordsOTMChildRepository(BaseRepository):
    model = RecordsOTMChildOrm
    mapper = RecordOTMChildDataMapper