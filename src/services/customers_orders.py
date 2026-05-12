from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.orders import OrdersRepository
from src.repositories.customers import CustomersRepository
from src.schemas.customers import Customer
from src.schemas.orders import Order
from src.repositories.mappers.mappers import OrderDataMapper
from src.schemas.customers_orders import CustomerOrderCreateRequest, CustomerOrdersGet, CustomerOrder
from src.schemas.customers import CustomerCreate
from src.schemas.orders import OrderCreate
from src.services.base import BaseService


class CustomerOrderService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(db)
        self.customers_repository = CustomersRepository(db)
        self.orders_repository = OrdersRepository(db)

    async def get_customer_orders(self, customer_id: UUID):
        customer_with_orders_model = await self.customers_repository.get_customer_with_orders(customer_id=customer_id)
        customer_with_orders = CustomerOrdersGet.model_validate(customer_with_orders_model, from_attributes=True)

        await self.db.commit()

        return customer_with_orders

    async def create_customer_order(self, customer_order_data: CustomerOrderCreateRequest):
        customer_model = await self.customers_repository.get_one_or_none(name=customer_order_data.customer.name)

        if customer_model:
            customer = Customer.model_validate(customer_model, from_attributes=True)

            order_to_create = OrderCreate(customer_id=customer.id, order_article=customer_order_data.order.order_article)
            created_order_model = await self.orders_repository.create(order_to_create)
            created_order = Order.model_validate(created_order_model, from_attributes=True)

            customer_order = CustomerOrder(customer=customer.model_dump(), order=created_order.model_dump())

            await self.db.commit()

            return customer_order
        else:
            customer_to_create = CustomerCreate(name=customer_order_data.customer.name)
            created_customer_model = await self.customers_repository.create(customer_to_create)
            created_customer = Customer.model_validate(created_customer_model, from_attributes=True)

            order_to_create = OrderCreate(customer_id=created_customer.id, order_article=customer_order_data.order.order_article)
            created_order_model = await self.orders_repository.create(order_to_create)
            created_order = Order.model_validate(created_order_model, from_attributes=True)

            customer_order = CustomerOrder(customer=created_customer.model_dump(), order=created_order.model_dump())

            await self.db.commit()

            return customer_order

    async def edit_customer_order(self, order_id: UUID, customer_order_data: CustomerOrderCreateRequest):
        order_model = await self.orders_repository.get_one_or_none(id=order_id)
        order = OrderDataMapper.map_to_domain_entity(order_model)

        updated_customer_model = await self.customers_repository.edit_one(data=customer_order_data.customer, id=order.customer_id)
        updated_customer = Customer.model_validate(updated_customer_model, from_attributes=True)

        updated_order_model = await self.orders_repository.edit_one(data=customer_order_data.order, id=order_id)
        updated_order = Order.model_validate(updated_order_model, from_attributes=True)

        customer_order = CustomerOrder(customer=updated_customer.model_dump(), order=updated_order.model_dump())

        await self.db.commit()

        return customer_order

    async def delete_customer_order(self, customer_id: UUID):
        deleted_customer_model = await self.customers_repository.delete(id=customer_id)
        deleted_customer = Customer.model_validate(deleted_customer_model, from_attributes=True)

        await self.orders_repository.delete_all(customer_id=deleted_customer.id)

        await self.db.commit()
        return deleted_customer

