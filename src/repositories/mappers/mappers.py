from src.schemas.records_otm_parent import RecordOTMParent
from src.models.orders import RecordsOTMParentOrm
from src.schemas.records_otm_child import RecordOTMChild
from src.models.customers import CustomersOrm
from src.models.records_mtm_child import RecordsMTMChildOrm, RecordsMTMParentChildOrm
from src.schemas.records_mtm_child import RecordMTMChildAdd, RecordMTMParentChildAdd, RecordMTMParentChild, \
    RecordMTMChild
from src.models.records_mtm_parent import RecordsMTMParentOrm
from src.models.drivers import DriversOrm
from src.models.licenses import LicensesOrm
from src.schemas.records_mtm_parent import RecordMTMParent, RecordMTMParentWithRels
from src.schemas.licenses import LicenseAdd
from src.repositories.mappers.base import DataMapper
from src.schemas.drivers import DriverAdd


class DriverDataMapper(DataMapper):
    db_model = DriversOrm
    schema = DriverAdd


class LicenseDataMapper(DataMapper):
    db_model = LicensesOrm
    schema = LicenseAdd

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
    db_model = CustomersOrm
    schema = RecordOTMChild

class RecordOTMParentDataMapper(DataMapper):
    db_model = RecordsOTMParentOrm
    schema = RecordOTMParent

