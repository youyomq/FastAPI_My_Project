from sqlalchemy.util import await_only

from src.schemas.records_otm_parent import RecordOTMParentRequestAdd
from src.schemas.records_otm_child import RecordOTMChildRequestAdd
from src.services.base import BaseService

class RecordOTMService(BaseService):
    async def add_one_child_otm_record(self, record_child_data: RecordOTMChildRequestAdd):
        await self.db.records_otm_child.add_one(child_value=record_child_data.child_value)

    async def get_all_child_otm_records(self):
        return await self.db.records_otm_child.get_all()

    async def edit_child_otm_record(self, record_child_data: RecordOTMChildRequestAdd, record_child_id: int):
        await self.db.records_otm_child.edit_one(data=record_child_data, id=record_child_id)

    async def delete_child_otm_record(self, record_child_id: int):
        await self.db.records_otm_child.delete(id=record_child_id)


    async def get_all_parent_otm_records(self):
        return await self.db.records_otm_parent.get_all()

    async def add_one_parent_otm_record(self, record_parent_data: RecordOTMParentRequestAdd):
        await self.db.records_otm_parent.add_one(parent_value=record_parent_data.parent_value, child_values=record_parent_data.child_values)