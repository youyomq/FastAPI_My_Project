from pydantic import BaseModel


class RecordMTMChildRequestAdd(BaseModel):
    child_value: str


class RecordMTMChildAdd(BaseModel):
    child_value: str


class RecordMTMChild(RecordMTMChildRequestAdd):
    id: int


class RecordMTMParentChildAdd(BaseModel):
    parent_id: int
    child_id: int

class RecordMTMParentChild(RecordMTMParentChildAdd):
    id: int

