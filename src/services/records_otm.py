from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentAdd, RecordOTMParentPutRequest
from src.schemas.records_otm_child import RecordOTMChildRequestAdd
from src.services.base import BaseService


class RecordOTMService(BaseService):
    async def add_parent_otm_record(self, record_parent_id: int, record_parent_data: RecordOTMParentRequestAdd):
        record_parent_to_add = RecordOTMParentAdd(parent_id=record_parent_id, **record_parent_data.model_dump())
        await self.db.records_otm_parent.add_one(record_parent_to_add)

    async def get_all_for_one_parent_record(self, record_parent_id: int):
        return await self.db.records_otm_parent.get_filtered(parent_id=record_parent_id)

    async def edit_parent_otm_record(self, record_id: int, record_parent_data: RecordOTMParentPutRequest):
        await self.db.records_otm_parent.edit_one(data=record_parent_data, id=record_id)

    async def delete_parent_otm_record(self, record_id: int):
        await self.db.records_otm_parent.delete(id=record_id)

    async def add_child_otm_record(self, record_child_data: RecordOTMChildRequestAdd):
        await self.db.records_otm_child.add_one(record_child_data)

    async def get_one_child_otm_record(self, record_child_id: int):
        return await self.db.records_otm_child.get_filtered(id=record_child_id)

    async def edit_one_child_otm_record(self, record_child_id: int, record_child_data: RecordOTMChildRequestAdd):
        await self.db.records_otm_child.edit_one(data=record_child_data, id=record_child_id)

    async def delete_one_otm_record(self, record_child_id: int):
        await self.db.records_otm_child.delete(id=record_child_id)