from pydantic import BaseModel


class RecordOTOChildRequestAdd(BaseModel):
    child_value: str


class RecordOTOChildAdd(RecordOTOChildRequestAdd):
    id: int

