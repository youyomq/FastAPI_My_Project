from uuid import UUID

from src.repositories.mappers.mappers import CustomerDataMapper, OrderDataMapper, CustomerOrdersDataMapper
from src.schemas.customers_orders import CustomerOrderRequestAdd
from src.schemas.customers import CustomerAdd
from src.schemas.orders import OrderAdd
from src.services.base import BaseService



class CustomerOrderService(BaseService):
    async def get_customer_orders(self, customer_id: UUID):
        customer_with_orders_model = await self.db.customers.get_customer_with_orders(customer_id=customer_id)
        customer_with_orders = CustomerOrdersDataMapper.map_to_domain_entity(customer_with_orders_model)
        return customer_with_orders

    async def add_customer_order(self, customer_order_data: CustomerOrderRequestAdd):
        customer_model = await self.db.customers.get_one_or_none(name=customer_order_data.customer.name)

        if customer_model:
            customer = CustomerDataMapper.map_to_domain_entity(data=customer_model)
            order_to_add = OrderAdd(customer_id=customer.id, order_article=customer_order_data.order.order_article)
            await self.db.orders.add(order_to_add)
        else:
            customer_to_add = CustomerAdd(name=customer_order_data.customer.name)
            added_customer = await self.db.customers.add(customer_to_add)
            order_to_add = OrderAdd(customer_id=added_customer.id, order_article=customer_order_data.order.order_article)
            await self.db.orders.add(order_to_add)


    async def edit_customer_order(self, order_id: UUID, customer_order_data: CustomerOrderRequestAdd):
        order_model = await self.db.orders.get_one_or_none(id=order_id)
        order = OrderDataMapper.map_to_domain_entity(order_model)

        await self.db.customers.edit_one(data=customer_order_data.customer, id=order.customer_id)
        await self.db.orders.edit_one(data=customer_order_data.order, id=order_id)


    async def delete_customer_order(self, customer_id: UUID):
        await self.db.customers.delete(id=customer_id)


