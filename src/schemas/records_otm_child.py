from pydantic import BaseModel, ConfigDict


class RecordOTMChildRequestAdd(BaseModel):
    child_value: str


class RecordOTMChildAdd(BaseModel):
    child_value: str


class RecordOTMChild(RecordOTMChildRequestAdd):
    id: int


class RecordOTMParentChildAdd(BaseModel):
    parent_id: int
    child_id: int

class RecordOTMParentChild(RecordOTMParentChildAdd):
    id: int

