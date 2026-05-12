from uuid import UUID

from pydantic import BaseModel

class OrderCreateRequest(BaseModel):
    order_article: str

class OrderPutRequest(BaseModel):
    order_article: str

class OrderCreate(BaseModel):
    customer_id: UUID
    order_article: str

class Order(BaseModel):
    id: UUID
    customer_id: UUID
    order_article: str