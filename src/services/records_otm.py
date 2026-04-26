from uuid import UUID

from schemas.records_otm import RecordOTMRequestAdd
from schemas.records_otm_child import RecordOTMChildAdd
from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentAdd, RecordOTMParentPutRequest
from src.services.base import BaseService


class RecordOTMService(BaseService):
    async def get_one_otm_record(self, record_child_id: UUID):
        child = await self.db.records_otm_child.get_filtered(id=record_child_id)
        parent = await self.db.records_otm_parent.get_filtered()

    async def add_otm_record(self, record_data: RecordOTMRequestAdd):
        child_record_to_add = RecordOTMChildAdd(child_value=record_data.child.child_value)
        added_child_record = await self.db.records_otm_child.add_one(child_record_to_add)

        record_parent_data = RecordOTMParentAdd(parent_id=record_parent_id,
                                                parent_value=record_data.parent.parent_value,
                                                fk_id=added_child_record.id)

        parent_record_to_add = RecordOTMParentAdd(parent_id=record_parent_id, **record_parent_data.model_dump())

        print(record_data)

        await self.db.records_otm_parent.add_one(parent_record_to_add)

    #async def edit_otm_record(self, record_id: UUID, record_data: RecordOTMRequest):
    #    await self.db.records_otm_parent.edit_one(data=record_parent_data, id=record_id)

    async def delete_otm_record(self, record_id: UUID):
        await self.db.records_otm_parent.delete(id=record_id)


