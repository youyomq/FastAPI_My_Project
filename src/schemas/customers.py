from uuid import UUID

from pydantic import BaseModel

class CustomerRequestAdd(BaseModel):
    name: str

class CustomerAdd(BaseModel):
    name: str

class Customer(CustomerAdd):
    id: UUID


