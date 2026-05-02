from uuid import UUID

from fastapi import APIRouter

from src.schemas.answers import StatusOkWithData, StatusOk
from src.schemas.customers_orders import CustomerOrderRequestAdd, CustomerOrdersGet
from src.services.customers_orders import CustomerOrderService
from src.dependencies import DBDep

router = APIRouter(prefix="/customers_orders", tags=["Customers Orders OTM Relationship"])

@router.get("/{customer_id}", response_model=StatusOkWithData[CustomerOrdersGet])
async def get_customer_orders(
        db: DBDep,
        customer_id: UUID
):
    customer_orders = await CustomerOrderService(db).get_customer_orders(customer_id)

    return {"status": "ok", "data": customer_orders}


@router.post("/", response_model=StatusOk, status_code=201)
async def add_customer_order(
        db: DBDep,
        customer_order_data: CustomerOrderRequestAdd
):
    await CustomerOrderService(db).add_customer_order(customer_order_data=customer_order_data)
    await db.commit()

    return {"status": "ok"}


@router.put("/{customer_id}", response_model=StatusOk)
async def edit_customer_order(
        db: DBDep,
        order_id: UUID,
        customer_order_data: CustomerOrderRequestAdd
):
    await CustomerOrderService(db).edit_customer_order(order_id=order_id, customer_order_data=customer_order_data)
    await db.commit()

    return {"status": "ok"}


@router.delete("/{customer_id}", status_code=204)
async def delete_customer_order(
        db: DBDep,
        customer_id: UUID,
):
    await CustomerOrderService(db).delete_customer_order(customer_id)
    await db.commit()






