from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models.customers import CustomersOrm
from src.repositories.base import BaseRepository


class CustomersRepository(BaseRepository):
    model = CustomersOrm

    async def get_customer_with_orders(self, customer_id: UUID):
        query = (
            select(self.model)
            .options(selectinload(self.model.orders))
            .filter_by(id=customer_id, is_deleted=False)
        )

        result = await self.session.execute(query)
        model = result.scalar()

        return model