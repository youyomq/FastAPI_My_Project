from pydantic import BaseModel, model_validator


class RecordOTOParentRequestAdd(BaseModel):
    parent_value: str
    fk_id: int


class RecordOTOParentAdd(BaseModel):
    id: int
    fk_id: int
    parent_value: str