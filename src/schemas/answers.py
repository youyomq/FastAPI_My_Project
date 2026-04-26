from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")

class StatusOk(BaseModel):
    status: str = "ok"

class StatusOkWithData(BaseModel, Generic[T]):
    status: str = "ok"
    data: T