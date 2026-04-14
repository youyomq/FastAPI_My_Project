from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from src.models.records_otm_parent import RecordsOTMParentOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordOTMParentDataMapper, RecordsOTMParentChildDataMapper


class RecordsOTMParentRepository(BaseRepository):
    model = RecordsOTMParentOrm
    mapper = RecordOTMParentDataMapper

    async def get_one_parent_records_with_rels(self, **filter_by):
        query = (
            select(self.model)
            .options(selectinload(self.model.child_values))
            .filter_by(**filter_by)
        )

        result = await self.session.execute(query)
        model = result.scalars().one()

        return RecordsOTMParentChildDataMapper.map_to_domain_entity(model)
