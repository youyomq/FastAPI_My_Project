from src.models.records_otm_parent import RecordsOTMParentOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTMParentDataMapper


class RecordsOTMParentRepository(BaseRepository):
    model = RecordsOTMParentOrm
    mapper = RecordOTMParentDataMapper