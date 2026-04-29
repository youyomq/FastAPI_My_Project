from uuid import UUID

from repositories.mappers.mappers import CustomerDataMapper, OrderDataMapper
from schemas.customers_orders import CustomerOrderRequestAdd, CustomerOrderGet
from schemas.customers import CustomerAdd
from src.schemas.orders import OrderAdd
from src.services.base import BaseService



class CustomerOrderService(BaseService):
    async def get_customer_orders(self, customer_id: UUID):
        customer_model = await self.db.customers.get_one_or_none(id=customer_id)
        customer = CustomerDataMapper.map_to_domain_entity(customer_model)

        orders_model = await self.db.orders.get_filtered(customer_id=customer_id)
        orders = [OrderDataMapper.map_to_domain_entity(order) for order in orders_model]

        customer_order = CustomerOrderGet(customer=customer, orders=orders)

        return customer_order

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

        customer_model = await self.db.customers.get_one_or_none(id=order.customer_id)
        customer = CustomerDataMapper.map_to_domain_entity(customer_model)

        if customer.name == customer_order_data.customer.name:
            await self.db.orders.edit_one(data=customer_order_data.order, id=order_id)
        else:
            await self.db.customers.edit_one(data=customer_order_data.customer, id=order.customer_id)
            await self.db.orders.edit_one(data=customer_order_data.order, id=order_id)


    async def delete_customer_order(self, customer_id: UUID):
        await self.db.orders.delete_all(customer_id=customer_id)
        await self.db.customers.delete(id=customer_id)


