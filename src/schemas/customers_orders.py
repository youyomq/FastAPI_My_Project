from uuid import UUID

from pydantic import BaseModel

from src.schemas.customers import CustomerCreateRequest, CustomerCreate, Customer
from src.schemas.orders import OrderCreateRequest, OrderCreate, Order


class CustomerOrderCreateRequest(BaseModel):
    customer: CustomerCreateRequest | None
    order: OrderCreateRequest

class CustomerOrderCreate(BaseModel):
    customer: CustomerCreate
    order: OrderCreate

class CustomerOrdersGet(BaseModel):
    id: UUID
    name: str
    orders: list[Order]

class CustomerOrder(CustomerOrderCreate):
    customer: Customer
    order: Order

