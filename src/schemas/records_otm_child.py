from uuid import UUID

from pydantic import BaseModel

class RecordOTMChildRequestAdd(BaseModel):
    child_value: str

class RecordOTMChildAdd(BaseModel):
    child_value: str

class RecordOTMChild(RecordOTMChildAdd):
    id: UUID


