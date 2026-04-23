from uuid import UUID

from src.schemas.records_oto import RecordOTORequestAdd, RecordOTO
from src.schemas.records_oto_parent import RecordOTOParentAdd, RecordOTOParentRequestAdd
from src.services.base import BaseService

class RecordOTOService(BaseService):
    async def get_one_oto_record(self, record_parent_id: UUID):
        parent_records = await self.db.records_oto_parent.get_one_or_none(id=record_parent_id)
        child_records = await self.db.records_oto_child.get_one_or_none(id=parent_records.fk_id)

        res_record = RecordOTO(parent=parent_records.model_dump(), child=child_records.model_dump())
        return res_record


    async def add_one_oto_record(self, record_data: RecordOTORequestAdd):
        child_record = await self.db.records_oto_child.add_one(data=record_data.child)

        parent_data = RecordOTOParentAdd(
            parent_value=record_data.parent.parent_value,
            fk_id=child_record.id
        )

        await self.db.records_oto_parent.add_one(data=parent_data)


    async def edit_oto_record(self, record_parent_id: UUID, record_data:RecordOTORequestAdd):
        parent_updated = await self.db.records_oto_parent.edit_one(data=record_data.parent, id=record_parent_id)
        await self.db.records_oto_child.edit_one(data=record_data.child, id=parent_updated.fk_id)


    async def delete_oto_record(self, record_parent_id: UUID):
        deleted_parent = await self.db.records_oto_parent.delete(id=record_parent_id)
        await self.db.records_oto_child.delete(id=deleted_parent.fk_id)


