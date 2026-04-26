from uuid import UUID

from pydantic import BaseModel

class RecordOTMParentRequestAdd(BaseModel):
    parent_value: str

class RecordOTMParentPutRequest(BaseModel):
    parent_value: str

class RecordOTMParentAdd(BaseModel):
    parent_id: UUID
    parent_value: str
    fk_id: UUID

class RecordOTMParent(RecordOTMParentAdd):
    id: UUID