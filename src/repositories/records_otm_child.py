from src.models.records_otm_child import RecordsOTMChildOrm, RecordsOTMParentChildOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTMChildDataMapper, RecordsOTMParentChildDataMapper


class RecordsOTMChildRepository(BaseRepository):
    model = RecordsOTMChildOrm
    mapper = RecordOTMChildDataMapper


class RecordsOTMParentChildRepository(BaseRepository):
    model = RecordsOTMParentChildOrm
    mapper = RecordsOTMParentChildDataMapper


