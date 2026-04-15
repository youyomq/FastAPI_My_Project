from pydantic import BaseModel

class RecordOTMParentRequestAdd(BaseModel):
    parent_value: str
    fk_id: int

class RecordOTMParentPutRequest(BaseModel):
    parent_value: str


class RecordOTMParentAdd(BaseModel):
    parent_id: int
    parent_value: str
    fk_id: int

class RecordOTMParent(RecordOTMParentAdd):
    id: int