from models.records_oto_parent import RecordsParentOrm
from models.records_oto_child import RecordsChildOrm
from schemas.records_oto_child import RecordOTOChildAdd
from src.repositories.mappers.base import DataMapper
from src.schemas.records_oto_parent import RecordOTOParentAdd


class RecordParentDataMapper(DataMapper):
    db_model = RecordsParentOrm
    schema = RecordOTOParentAdd


class RecordChildDataMapper(DataMapper):
    db_model = RecordsChildOrm
    schema = RecordOTOChildAdd