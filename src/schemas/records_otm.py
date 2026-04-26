from pydantic import BaseModel, ConfigDict

from src.schemas.records_otm_child import RecordOTMChildRequestAdd, RecordOTMChildAdd
from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentAdd


class RecordOTMRequestAdd(BaseModel):
    child: RecordOTMChildRequestAdd
    parent: RecordOTMParentRequestAdd

class RecordOTMAdd(BaseModel):
    child: RecordOTMChildAdd
    parent: RecordOTMParentAdd

class RecordOTM(RecordOTMAdd):
    model_config = ConfigDict(from_attributes=True)
