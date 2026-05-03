from pydantic import BaseModel
from typing import TypeVar, Generic

from schemas.drivers_licenses import DriverLicense

T = TypeVar("T", bound=BaseModel)

class StatusOk(BaseModel):
    status: str = "ok"

class StatusOkWithData(BaseModel, Generic[T]):
    status: str = "ok"
    data: T
