from sqlalchemy import select, delete, update
from sqlalchemy.orm import selectinload


from src.models.records_mtm_child import RecordsMTMParentChildOrm
from src.repositories.records_mtm_child import RecordsMTMParentChildRepository
from src.schemas.records_mtm_child import RecordMTMParentChildAdd
from src.schemas.records_mtm_parent import RecordMTMParentRequestAdd, RecordMTMParentAdd
from src.models.records_mtm_parent import RecordsMTMParentOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RecordMTMParentDataMapper, RecordsMTMParentChildDataMapper


class RecordsMTMParentRepository(BaseRepository):
    model = RecordsMTMParentOrm
    mapper = RecordMTMParentDataMapper

    async def get_one_parent_records_with_rels(self, **filter_by):
        query = (
            select(self.model)
            .options(selectinload(self.model.child_values))
            .filter_by(**filter_by)
        )

        result = await self.session.execute(query)
        model = result.scalars().one()

        return RecordsMTMParentChildDataMapper.map_to_domain_entity(model)


    async def edit_bulk(self, parent_record_data: RecordMTMParentRequestAdd, record_parent_id: int):
        delete_parent_child_stmt = delete(RecordsMTMParentChildOrm).filter_by(parent_id=record_parent_id)
        await self.session.execute(delete_parent_child_stmt)

        update_parent_stmt = update(self.model).filter_by(id=record_parent_id).values(parent_value=parent_record_data.parent_value).returning(self.model)
        update_parent_record = await self.session.execute(update_parent_stmt)
        updated_parent_record = update_parent_record.scalars().one()


        child_ids_to_add = [RecordMTMParentChildAdd(parent_id=updated_parent_record.id, child_id=child_id) for child_id in parent_record_data.child_ids]

        if child_ids_to_add:
            await RecordsMTMParentChildRepository(self.session).add_bulk(data=child_ids_to_add)