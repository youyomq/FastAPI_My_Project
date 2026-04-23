from uuid import UUID

from fastapi import APIRouter

from src.schemas.answers import StatusOk, StatusOkWithData
from src.schemas.records_oto import RecordOTORequestAdd
from src.api.dependencies import DBDep
from src.services.records_oto import RecordOTOService


router = APIRouter(prefix="/records_oto", tags=["Records OTO Relationship"])

@router.get("/{record_parent_id}")
async def get_one_oto_record(
        db: DBDep,
        record_parent_id: UUID
):
    parent_record = await RecordOTOService(db).get_one_oto_record(record_parent_id)

    return StatusOkWithData(data=parent_record).answer_ok()



@router.post("/parent_record")
async def add_oto_record(
        db: DBDep,
        record_parent_data: RecordOTORequestAdd
):
    await RecordOTOService(db).add_one_oto_record(record_data=record_parent_data)
    await db.commit()

    return StatusOk.answer_ok()


@router.put("/parent_record/{record_parent_id}")
async def edit_oto_record(
        db: DBDep,
        record_parent_id: UUID,
        record_data: RecordOTORequestAdd
):
    await RecordOTOService(db).edit_oto_record(record_parent_id=record_parent_id, record_data=record_data)
    await db.commit()

    return StatusOk.answer_ok()



@router.delete("/parent_record/{record_parent_id}")
async def delete_oto_record(
        db: DBDep,
        record_parent_id: UUID
):
    await RecordOTOService(db).delete_oto_record(record_parent_id)
    await db.commit()

    return StatusOk.answer_ok()








