from typing import Sequence
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete


class BaseRepository:
    model = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)

        return [item for item in result.scalars().all()]


    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()

        return model


    async def add(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)

        result = await self.session.execute(stmt)
        model = result.scalars().one()

        return model

    async def add_all(self, data: Sequence[BaseModel]):
        add_stmt = insert(self.model).values([i.model_dump() for i in data])
        await self.session.execute(add_stmt)


    async def edit_one(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        stmt = (update(self.model)
                .filter_by(**filter_by)
                .values(data.model_dump(exclude_unset=exclude_unset))
                .returning(self.model)
                )
        result = await self.session.execute(stmt)
        model = result.scalars().one()

        return model


    async def delete(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(stmt)
        model = result.scalars().one()

        return model

    async def delete_all(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)

    async def delete_all_in_list(self, items_list: list[UUID]):
        stmt = delete(self.model).filter(self.model.id.in_(items_list))
        await self.session.execute(stmt)

