from pydantic import BaseModel

class RecordOTMChildRequestAdd(BaseModel):
    child_value: str


class RecordOTMChildAdd(RecordOTMChildRequestAdd):
    id: int
