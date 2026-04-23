from uuid import UUID
from pydantic import BaseModel


class RecordOTOChildRequestAdd(BaseModel):
    child_value: str


class RecordOTOChildAdd(BaseModel):
    id: UUID
    child_value: str

