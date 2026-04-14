from time import sleep
from typing import Sequence

from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete

from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session


    async def get_all(self):
        query = select(self.model)

        result = await self.session.execute(query)

        return [self.mapper.map_to_domain_entity(item) for item in result.scalars().all()]


    async def add_one(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)

        result = await self.session.execute(stmt)
        model = result.scalars().one()

        return self.mapper.map_to_domain_entity(model)

    async def add_bulk(self, data: Sequence[BaseModel]):
        add_stmt = insert(self.model).values([i.model_dump() for i in data])
        await self.session.execute(add_stmt)


    async def edit_one(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        stmt = (update(self.model)
                .filter_by(**filter_by)
                .values(data.model_dump(exclude_unset=exclude_unset)))

        await self.session.execute(stmt)

    async def edit_bulk(self, ):

    async def delete(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)

        await self.session.execute(stmt)