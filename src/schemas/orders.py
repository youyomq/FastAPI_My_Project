from uuid import UUID

from pydantic import BaseModel

class OrderRequestAdd(BaseModel):
    order_article: str

class OrderPutRequest(BaseModel):
    order_article: str

class OrderAdd(BaseModel):
    customer_id: UUID
    order_article: str

class Order(OrderAdd):
    id: UUID