from uuid import UUID

from pydantic import BaseModel


class DriverCreateRequest(BaseModel):
    name: str
    lastname: str


class DriverCreate(BaseModel):
    name: str
    lastname: str
    license_id: UUID

class Driver(BaseModel):
    id: UUID
    name: str
    lastname: str
    license_id: UUID


