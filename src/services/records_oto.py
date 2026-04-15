from src.schemas.records_oto_child import RecordOTOChildRequestAdd
from src.schemas.records_oto_parent import RecordOTOParentRequestAdd
from src.services.base import BaseService

class RecordOTOService(BaseService):
    async def get_all_parent_records(self):
        return await self.db.records_oto_parent.get_all()

    async def get_one_parent_record(self, record_parent_id: int):
        return await self.db.records_oto_parent.get_filtered(id=record_parent_id)

    async def get_all_child_records(self):
        return await self.db.records_oto_child.get_all()

    async def get_one_child_record(self, record_child_id: int):
        return await self.db.records_oto_child.get_filtered(id=record_child_id)

    async def add_one_child_record(self, record_child_data: RecordOTOChildRequestAdd):
        await self.db.records_oto_child.add_one(record_child_data)


    async def add_one_parent_record(self, record_parent_data: RecordOTOParentRequestAdd):
        await self.db.records_oto_parent.add_one(record_parent_data)

    async def edit_child_record(self, record_child_data: RecordOTOChildRequestAdd, record_child_id: int):
        await self.db.records_oto_child.edit_one(data=record_child_data, id=record_child_id)


    async def edit_parent_record(self, record_parent_data: RecordOTOParentRequestAdd, record_parent_id: int):
        await self.db.records_oto_parent.edit_one(data=record_parent_data, id=record_parent_id)


    async def delete_parent_oto_record(self, record_parent_id: int):
        await self.db.records_oto_parent.delete(id=record_parent_id)


    async def delete_child_oto_record(self, record_child_id: int):
        await self.db.records_oto_child.delete(id=record_child_id)