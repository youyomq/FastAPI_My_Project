from uuid import UUID

from pydantic import BaseModel


class DriverRequestAdd(BaseModel):
    name: str
    lastname: str


class DriverAdd(BaseModel):
    name: str
    lastname: str
    license_id: UUID
