from uuid import UUID

from pydantic import BaseModel, Field


class RecordOTOParentRequestAdd(BaseModel):
    parent_value: str


class RecordOTOParentAdd(BaseModel):
    fk_id: UUID
    parent_value: str