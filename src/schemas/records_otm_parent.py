from pydantic import BaseModel, ConfigDict

from src.schemas.records_otm_child import RecordOTMChild


class RecordOTMParentRequestAdd(BaseModel):
    parent_value: str
    child_ids: list[int] = []


class RecordOTMParentAdd(BaseModel):
    parent_value: str


class RecordOTMParent(RecordOTMParentAdd):
    id: int
    parent_value: str

class RecordOTMParentWithRels(RecordOTMParentAdd):
    id: int
    parent_value: str
    child_values: list[RecordOTMChild]
