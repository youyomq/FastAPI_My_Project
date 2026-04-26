from uuid import UUID

from fastapi import APIRouter

from schemas.records_otm import RecordOTMRequestAdd
from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentPutRequest
from src.schemas.records_otm_child import RecordOTMChildRequestAdd
from src.services.records_otm import RecordOTMService
from src.core.dependencies import DBDep

router = APIRouter(prefix="/records_otm", tags=["Records OTM Relationship"])

@router.get("/child_record/{record_child_id}")
async def get_one_child_otm_record(
        db: DBDep,
        record_child_id: UUID
):
    child_record = await RecordOTMService(db).get_one_otm_record(record_child_id)

    return {"status": "ok", "data": child_record}


@router.post("/parent_record")
async def add_one_parent_record(
        db: DBDep,
        record_data: RecordOTMRequestAdd
):
    await RecordOTMService(db).add_otm_record(record_data=record_data)
    await db.commit()

    return {"status": "ok"}


#@router.put("/parent_record/{record_parent_id}")
#async def edit_parent_otm_record(
#        db: DBDep,
#        record_id: UUID,
#        record_data: RecordOTMParentPutRequest
#):
#    await RecordOTMService(db).edit_otm_record(record_id=record_id, record_parent_data=record_parent_data)
#    await db.commit()
#
#    return {"status": "ok"}
#
#
#@router.delete("/parent_record/{record_parent_id}")
#async def delete_parent_otm_record(
#        db: DBDep,
#        record_id: UUID,
#):
#    await RecordOTMService(db).delete_otm_record(record_id)
#    await db.commit()
#
#    return {"status": "ok"}






