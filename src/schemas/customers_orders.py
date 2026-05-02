from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.schemas.customers import CustomerRequestAdd, CustomerAdd, Customer
from src.schemas.orders import OrderRequestAdd, OrderAdd, Order


class CustomerOrderRequestAdd(BaseModel):
    customer: CustomerRequestAdd | None
    order: OrderRequestAdd

class CustomerOrderAdd(BaseModel):
    customer: CustomerAdd
    order: OrderAdd

class CustomerOrdersGet(BaseModel):
    id: UUID
    name: str
    orders: list[Order]

class CustomerOrder(CustomerOrderAdd):
    model_config = ConfigDict(from_attributes=True)
