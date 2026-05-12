from uuid import UUID

from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):
    name: str

class CustomerCreate(BaseModel):
    name: str

class Customer(BaseModel):
    id: UUID
    name: str


