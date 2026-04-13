from pydantic import BaseModel


class RecordOTOChildRequestAdd(BaseModel):
    child_value: str


class RecordOTOChildAdd(BaseModel):
    id: int
    child_value: str

