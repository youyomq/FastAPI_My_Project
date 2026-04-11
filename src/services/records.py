from schemas.records_oto_child import RecordOTOChildRequestAdd, RecordOTOChildAdd
from schemas.records_oto_parent import RecordOTOParentRequestAdd
from src.services.base import BaseService

class RecordService(BaseService):
    async def get_all_parent_records(self):
        return await self.db.records_parent.get_all()


    async def get_all_child_records(self):
        return await self.db.records_child.get_all()


    async def add_one_child_record(self, record_child_data: RecordOTOChildRequestAdd):
        await self.db.records_child.add_one(child_value=record_child_data.child_value)


    async def add_one_parent_record(self, record_parent_data: RecordOTOParentRequestAdd):
        await self.db.records_parent.add_one(fk_id=record_parent_data.fk_id, parent_value=record_parent_data.parent_value)


    async def edit_child_record(self, record_child_data: RecordOTOChildRequestAdd, record_child_id: int):
        await self.db.records_child.edit_one(data=record_child_data, id=record_child_id)


    async def edit_parent_record(self, record_parent_data: RecordOTOParentRequestAdd, record_parent_id: int):
        await self.db.records_parent.edit_one(data=record_parent_data, id=record_parent_id)


    async def delete_parent_oto_record(self, record_parent_id: int):
        await self.db.records_parent.delete(id=record_parent_id)


    async def delete_child_oto_record(self, record_child_id: int):
        await self.db.records_child.delete(id=record_child_id)