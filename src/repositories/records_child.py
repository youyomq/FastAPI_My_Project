from models.records_oto_child import RecordsChildOrm
from repositories.base import BaseRepository
from repositories.mappers.mappers import RecordChildDataMapper


class RecordsChildRepository(BaseRepository):
    model = RecordsChildOrm
    mapper = RecordChildDataMapper