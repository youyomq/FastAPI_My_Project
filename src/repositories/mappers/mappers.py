from src.models.records_otm_child import RecordsOTMChildOrm
from src.schemas.records_otm_child import RecordOTMChildAdd
from src.models.records_otm_parent import RecordsOTMParentOrm
from src.models.records_oto_parent import RecordsOTOParentOrm
from src.models.records_oto_child import RecordsOTOChildOrm
from src.schemas.records_otm_parent import RecordOTMParentAdd
from src.schemas.records_oto_child import RecordOTOChildAdd
from src.repositories.mappers.base import DataMapper
from src.schemas.records_oto_parent import RecordOTOParentAdd


class RecordOTOParentDataMapper(DataMapper):
    db_model = RecordsOTOParentOrm
    schema = RecordOTOParentAdd


class RecordOTOChildDataMapper(DataMapper):
    db_model = RecordsOTOChildOrm
    schema = RecordOTOChildAdd


class RecordOTMParentDataMapper(DataMapper):
    db_model = RecordsOTMParentOrm
    schema = RecordOTMParentAdd


class RecordOTMChildDataMapper(DataMapper):
    db_model = RecordsOTMChildOrm
    schema = RecordOTMChildAdd
