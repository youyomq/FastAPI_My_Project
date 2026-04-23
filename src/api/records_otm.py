from uuid import UUID

from fastapi import APIRouter

from src.schemas.records_otm_parent import RecordOTMParentRequestAdd, RecordOTMParentPutRequest
from src.schemas.records_otm_child import RecordOTMChildRequestAdd
from src.services.records_otm import RecordOTMService
from src.api.dependencies import DBDep

router = APIRouter(prefix="/records_otm", tags=["Records OTM Relationship"])

@router.post("/parent_record")
async def add_one_parent_record(
        db: DBDep,
        record_parent_id: UUID,
        record_parent_data: RecordOTMParentRequestAdd
):
    await RecordOTMService(db).add_parent_otm_record(record_parent_id=record_parent_id,record_parent_data=record_parent_data)
    await db.commit()

    return {"status": "ok"}

@router.get("/parent_record/{record_parent_id}")
async def get_all_for_one_parent_record(
        db: DBDep,
        record_parent_id: UUID
):
    record_parent = await RecordOTMService(db).get_all_for_one_parent_record(record_parent_id)

    return {"status": "ok", "data": record_parent}


@router.put("/parent_record/{record_parent_id}")
async def edit_parent_otm_record(
        db: DBDep,
        record_id: UUID,
        record_parent_data: RecordOTMParentPutRequest
):
    await RecordOTMService(db).edit_parent_otm_record(record_id=record_id, record_parent_data=record_parent_data)
    await db.commit()

    return {"status": "ok"}


@router.delete("/parent_record/{record_parent_id}")
async def delete_parent_otm_record(
        db: DBDep,
        record_id: UUID,
):
    await RecordOTMService(db).delete_parent_otm_record(record_id)
    await db.commit()

    return {"status": "ok"}


@router.get("/child_record/{record_child_id}")
async def get_one_child_otm_record(
    db: DBDep,
    record_child_id: UUID
):
    child_record = await RecordOTMService(db).get_one_child_otm_record(record_child_id)

    return {"status": "ok", "data": child_record}

@router.post("/child_record")
async def add_child_otm_child_record(
        db: DBDep,
        record_child_data: RecordOTMChildRequestAdd
):
    await RecordOTMService(db).add_child_otm_record(record_child_data)
    await db.commit()

    return {"status": "ok"}

@router.put("/child_record/{record_child_id}")
async def edit_one_otm_child_record(
        db: DBDep,
        record_child_data: RecordOTMChildRequestAdd,
        record_child_id: UUID
):
    await RecordOTMService(db).edit_one_child_otm_record(record_child_id=record_child_id, record_child_data=record_child_data)
    await db.commit()

    return {"status": "ok"}

@router.delete("/child_record/{record_child_id}")
async def delete_one_child_record(
        db: DBDep,
        record_child_id: UUID
):
    await RecordOTMService(db).delete_one_otm_record(record_child_id)
    await db.commit()

    return {"status": "ok"}


