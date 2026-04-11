from models.records_oto_parent import RecordsParentOrm
from repositories.mappers.mappers import RecordParentDataMapper
from src.repositories.base import BaseRepository

class RecordsParentRepository(BaseRepository):
    model = RecordsParentOrm
    mapper = RecordParentDataMapper
