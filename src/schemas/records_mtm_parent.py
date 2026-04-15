from pydantic import BaseModel, ConfigDict

from src.schemas.records_mtm_child import RecordMTMChild


class RecordMTMParentRequestAdd(BaseModel):
    parent_value: str
    child_ids: list[int] | None = []


class RecordMTMParentAdd(BaseModel):
    parent_value: str


class RecordMTMParent(RecordMTMParentAdd):
    id: int
    parent_value: str

class RecordMTMParentWithRels(RecordMTMParentAdd):
    id: int
    parent_value: str
    child_values: list[RecordMTMChild]
