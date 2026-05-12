from uuid import UUID

from fastapi import APIRouter

from schemas.customers import Customer
from src.schemas.customers_orders import CustomerOrderCreateRequest, CustomerOrdersGet, CustomerOrder
from src.services.customers_orders import CustomerOrderService
from src.dependencies import DBDep

router = APIRouter(prefix="/customers_orders", tags=["Customers Orders OTM Relationship"])

@router.get("/{customer_id}", response_model=CustomerOrdersGet)
async def get_customer_orders(
        db: DBDep,
        customer_id: UUID
):
    return await CustomerOrderService(db).get_customer_orders(customer_id)


@router.post("/", response_model=CustomerOrder, status_code=201)
async def create_customer_order(
        db: DBDep,
        customer_order_data: CustomerOrderCreateRequest
):
    return await CustomerOrderService(db).create_customer_order(customer_order_data=customer_order_data)


@router.put("/{customer_id}", response_model=CustomerOrder, status_code=200)
async def edit_customer_order(
        db: DBDep,
        order_id: UUID,
        customer_order_data: CustomerOrderCreateRequest
):
    return await CustomerOrderService(db).edit_customer_order(order_id=order_id, customer_order_data=customer_order_data)


@router.delete("/{customer_id}", response_model=Customer, status_code=200)
async def delete_customer_order(
        db: DBDep,
        customer_id: UUID,
):
    return await CustomerOrderService(db).delete_customer_order(customer_id)
