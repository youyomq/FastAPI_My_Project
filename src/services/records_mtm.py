from sqlalchemy.util import await_only

from src.schemas.records_mtm_parent import RecordMTMParentRequestAdd, RecordMTMParentAdd
from src.schemas.records_mtm_child import RecordMTMChildRequestAdd, RecordMTMParentChildAdd
from src.services.base import BaseService

class RecordMTMService(BaseService):
    async def add_one_child_mtm_record(self, record_child_data: RecordMTMChildRequestAdd):
        await self.db.records_mtm_child.add_one(record_child_data)

    async def get_all_child_mtm_records(self):
        return await self.db.records_mtm_child.get_all()

    async def get_one_child_record(self, record_child_id: int):
        return await self.db.records_mtm_child.get_filtered(id=record_child_id)

    async def edit_child_mtm_record(self, record_child_data: RecordMTMChildRequestAdd, record_child_id: int):
        await self.db.records_mtm_child.edit_one(data=record_child_data, id=record_child_id)

    async def delete_child_mtm_record(self, record_child_id: int):
        await self.db.records_mtm_child.delete(id=record_child_id)

    async def get_one_parent_mtm_record(self, record_parent_id: int):
        return await self.db.records_mtm_parent.get_one_parent_records_with_rels(id=record_parent_id)

    async def add_one_parent_mtm_record(self, record_parent_data: RecordMTMParentRequestAdd):
        record_parent_data_schema = RecordMTMParentAdd(**record_parent_data.model_dump())

        record_parent = await self.db.records_mtm_parent.add_one(record_parent_data_schema)

        records_parent_child =[
            RecordMTMParentChildAdd(parent_id=record_parent.id, child_id=child_id)
            for child_id in record_parent_data.child_ids
        ]

        await self.db.records_mtm_parent_child.add_bulk(records_parent_child)

    async def delete_parent_mtm_record(self, record_parent_id: int):
        await self.db.records_mtm_parent_child.delete(parent_id=record_parent_id)
        await self.db.records_mtm_parent.delete(id=record_parent_id)

    async def edit_one_parent_mtm_record(self, parent_record_data: RecordMTMParentRequestAdd, record_parent_id: int):
        await self.db.records_mtm_parent.edit_bulk(parent_record_data=parent_record_data, record_parent_id=record_parent_id)