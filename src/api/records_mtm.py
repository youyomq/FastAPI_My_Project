from fastapi import APIRouter

from src.schemas.records_mtm_parent import RecordMTMParentRequestAdd
from src.services.records_mtm import RecordMTMService
from src.schemas.records_mtm_child import RecordMTMChildRequestAdd
from src.api.dependencies import DBDep

router = APIRouter(prefix="/records_mtm", tags=["Records MTM Relationship"])

@router.get("/record_parent/{record_parent_id}")
async def get_one_parent_mtm_record(
        db: DBDep,
        record_parent_id: int
):
    parent_records = await RecordMTMService(db).get_one_parent_mtm_record(record_parent_id=record_parent_id)

    return {"status": "ok", "data": parent_records}


@router.post("/record_parent")
async def add_one_parent_mtm_records(
        db: DBDep,
        record_parent_data: RecordMTMParentRequestAdd
):
    await RecordMTMService(db).add_one_parent_mtm_record(record_parent_data)
    await db.commit()

    return {"status": "ok"}


@router.put("/record_parent/{record_parent_id}")
async def edit_one_parent_mtm_record(
        db: DBDep,
        record_parent_id: int,
        parent_record_data: RecordMTMParentRequestAdd
):
    await RecordMTMService(db).edit_one_parent_mtm_record(parent_record_data=parent_record_data, record_parent_id=record_parent_id)
    await db.commit()

    return {"status": "ok"}

@router.delete("/record_parent/{record_parent_id}")
async def delete_one_parent_mtm_records(
        db: DBDep,
        record_parent_id: int
):
    await RecordMTMService(db).delete_parent_mtm_record(record_parent_id=record_parent_id)
    await db.commit()

    return {"status": "ok"}


@router.get("/record_child")
async def get_all_child_mtm_records(
        db: DBDep
):
    child_records = await RecordMTMService(db).get_all_child_mtm_records()

    return {"status": "ok", "data": child_records}


@router.get("/child_record/{record_child_id}")
async def get_one_child_mtm_record(
        db: DBDep,
        record_child_id: int
):
    child_record = await RecordMTMService(db).get_one_child_record(record_child_id)

    return {"status": "ok", "data": child_record}


@router.post("/record_child")
async def add_one_child_mtm_record(
        db: DBDep,
        record_child_data: RecordMTMChildRequestAdd
):
    await RecordMTMService(db).add_one_child_mtm_record(record_child_data)
    await db.commit()
    return {"status": "ok"}


@router.put("/record_child/{record_child_id}")
async def edit_child_mtm_record(
        db: DBDep,
        record_child_id: int,
        record_child_data: RecordMTMChildRequestAdd
):
    await RecordMTMService(db).edit_child_mtm_record(record_child_data=record_child_data, record_child_id=record_child_id)
    await db.commit()

    return {"status": "ok"}


@router.delete("/record_child/{record_child_id}")
async def delete_child_mtm_record(
        db: DBDep,
        record_child_id: int
):
    await RecordMTMService(db).delete_child_mtm_record(record_child_id=record_child_id)
    await db.commit()

    return {"status": "ok"}



