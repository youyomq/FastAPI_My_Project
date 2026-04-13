from pydantic import BaseModel

class RecordOTMParentRequestAdd(BaseModel):
    parent_value: str
    child_values: list


class RecordOTMParentAdd(BaseModel):
    id: int
    parent_value: str
    child_values: list