from pydantic import BaseModel, ConfigDict

from schemas.records_oto_child import RecordOTOChildRequestAdd, RecordOTOChildAdd
from schemas.records_oto_parent import RecordOTOParentRequestAdd, RecordOTOParentAdd


class RecordOTORequestAdd(BaseModel):
    parent: RecordOTOParentRequestAdd
    child: RecordOTOChildRequestAdd


class RecordOTOAdd(BaseModel):
    parent: RecordOTOParentAdd
    child: RecordOTOChildAdd


class RecordOTO(RecordOTOAdd):
    model_config = ConfigDict(from_attributes=True)