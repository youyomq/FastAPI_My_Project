from src.models.records_mtm_child import RecordsMTMChildOrm, RecordsMTMParentChildOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordMTMChildDataMapper, RecordsMTMParentChildDataMapper


class RecordsMTMChildRepository(BaseRepository):
    model = RecordsMTMChildOrm
    mapper = RecordMTMChildDataMapper


class RecordsMTMParentChildRepository(BaseRepository):
    model = RecordsMTMParentChildOrm
    mapper = RecordsMTMParentChildDataMapper


