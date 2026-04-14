from src.models.records_otm_child import RecordsOTMChildOrm, RecordsOTMParentChildOrm
from src.schemas.records_otm_child import RecordOTMChildAdd, RecordOTMParentChildAdd, RecordOTMParentChild, \
    RecordOTMChild
from src.models.records_otm_parent import RecordsOTMParentOrm
from src.models.records_oto_parent import RecordsOTOParentOrm
from src.models.records_oto_child import RecordsOTOChildOrm
from src.schemas.records_otm_parent import RecordOTMParent, RecordOTMParentWithRels
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
    schema = RecordOTMParent


class RecordOTMChildDataMapper(DataMapper):
    db_model = RecordsOTMChildOrm
    schema = RecordOTMChild

class RecordsOTMParentChildDataMapper(DataMapper):
    db_model = RecordsOTMParentChildOrm
    schema = RecordOTMParentWithRels
