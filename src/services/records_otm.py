from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentAdd
from src.schemas.records_otm_child import RecordOTMChildRequestAdd, RecordOTMParentChildAdd
from src.services.base import BaseService

class RecordOTMService(BaseService):
    async def add_one_child_otm_record(self, record_child_data: RecordOTMChildRequestAdd):
        await self.db.records_otm_child.add_one(record_child_data)

    async def get_all_child_otm_records(self):
        return await self.db.records_otm_child.get_all()

    async def edit_child_otm_record(self, record_child_data: RecordOTMChildRequestAdd, record_child_id: int):
        await self.db.records_otm_child.edit_one(data=record_child_data, id=record_child_id)

    async def delete_child_otm_record(self, record_child_id: int):
        await self.db.records_otm_child.delete(id=record_child_id)

    async def get_one_parent_otm_record(self, record_parent_id: int):
        return await self.db.records_otm_parent.get_one_parent_records_with_rels(id=record_parent_id)

    async def add_one_parent_otm_record(self, record_parent_data: RecordOTMParentRequestAdd):
        record_parent_data_schema = RecordOTMParentAdd(**record_parent_data.model_dump())

        record_parent = await self.db.records_otm_parent.add_one(record_parent_data_schema)

        records_parent_child =[
            RecordOTMParentChildAdd(parent_id=record_parent.id, child_id=child_id)
            for child_id in record_parent_data.child_ids
        ]

        await self.db.records_otm_parent_child.add_bulk(records_parent_child)

    async def delete_parent_otm_record(self, record_parent_id: int):
        await self.db.records_otm_parent_child.delete(parent_id=record_parent_id)
        await self.db.records_otm_parent.delete(id=record_parent_id)

    async def edit_one_parent_otm_record(self):
        await self.db.records_otm_parent_child.edit_bulk()