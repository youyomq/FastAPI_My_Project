from src.schemas.records_otm_parent import RecordOTMParent
from src.models.records_otm_parent import RecordsOTMParentOrm
from src.schemas.records_otm_child import RecordOTMChild
from src.models.records_otm_child import RecordsOTMChildOrm
from src.models.records_mtm_child import RecordsMTMChildOrm, RecordsMTMParentChildOrm
from src.schemas.records_mtm_child import RecordMTMChildAdd, RecordMTMParentChildAdd, RecordMTMParentChild, \
    RecordMTMChild
from src.models.records_mtm_parent import RecordsMTMParentOrm
from src.models.records_oto_parent import RecordsOTOParentOrm
from src.models.records_oto_child import RecordsOTOChildOrm
from src.schemas.records_mtm_parent import RecordMTMParent, RecordMTMParentWithRels
from src.schemas.records_oto_child import RecordOTOChildAdd
from src.repositories.mappers.base import DataMapper
from src.schemas.records_oto_parent import RecordOTOParentAdd


class RecordOTOParentDataMapper(DataMapper):
    db_model = RecordsOTOParentOrm
    schema = RecordOTOParentAdd


class RecordOTOChildDataMapper(DataMapper):
    db_model = RecordsOTOChildOrm
    schema = RecordOTOChildAdd

class RecordMTMParentDataMapper(DataMapper):
    db_model = RecordsMTMParentOrm
    schema = RecordMTMParent


class RecordMTMChildDataMapper(DataMapper):
    db_model = RecordsMTMChildOrm
    schema = RecordMTMChild

class RecordsMTMParentChildDataMapper(DataMapper):
    db_model = RecordsMTMParentChildOrm
    schema = RecordMTMParentWithRels


class RecordOTMChildDataMapper(DataMapper):
    db_model = RecordsOTMChildOrm
    schema = RecordOTMChild

class RecordOTMParentDataMapper(DataMapper):
    db_model = RecordsOTMParentOrm
    schema = RecordOTMParent

