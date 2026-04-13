from src.models.records_oto_parent import RecordsOTOParentOrm
from src.repositories.mappers.mappers import RecordOTOParentDataMapper
from src.repositories.base import BaseRepository

class RecordsOTOParentRepository(BaseRepository):
    model = RecordsOTOParentOrm
    mapper = RecordOTOParentDataMapper
