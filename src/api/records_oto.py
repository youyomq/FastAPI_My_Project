from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.records_oto_child import RecordOTOChildRequestAdd
from src.schemas.records_oto_parent import RecordOTOParentRequestAdd
from src.services.records_oto import RecordOTOService


router = APIRouter(prefix="/records_oto", tags=["Records OTO Relationship"])


@router.get("/parent_record")
async def get_all_parent_oto_records(
        db: DBDep
):
    parent_records = await RecordOTOService(db).get_all_parent_records()

    return {"status": "ok", "data": parent_records}


@router.get("/parent_record/{record_parent_id}")
async def get_one_parent_oto_record(
        db: DBDep,
        record_parent_id: int
):
    parent_record = await RecordOTOService(db).get_one_parent_record(record_parent_id)

    return {"status": "ok", "data": parent_record}


@router.post("/parent_record")
async def add_parent_oto_record(
        db: DBDep,
        record_parent_data: RecordOTOParentRequestAdd
):
    await RecordOTOService(db).add_one_parent_record(record_parent_data)
    await db.commit()
    return {"status": "ok"}


@router.put("/parent_record/{record_parent_id}")
async def edit_parent_oto_record(
        db: DBDep,
        record_parent_id: int,
        record_parent_data: RecordOTOParentRequestAdd
):
    await RecordOTOService(db).edit_parent_record(record_parent_id=record_parent_id, record_parent_data=record_parent_data)
    await db.commit()

    return {"status": "ok"}


@router.delete("/parent_record/{record_parent_id}")
async def delete_parent_oto_record(
        db: DBDep,
        record_parent_id: int
):
    await RecordOTOService(db).delete_parent_oto_record(record_parent_id)
    await db.commit()

    return {"status": "ok"}


@router.get("/child_record/")
async def get_all_child_oto_records(
        db: DBDep
):
    child_records = await RecordOTOService(db).get_all_child_records()

    return {"status": "ok", "data": child_records}


@router.get("/child_record/{record_child_id}")
async def get_one_child_oto_record(
        db: DBDep,
        record_child_id: int
):
    child_record = await RecordOTOService(db).get_one_child_record(record_child_id)

    return {"status": "ok", "data": child_record}


@router.post("/child_record")
async def add_child_oto_record(
        db: DBDep,
        record_child_data: RecordOTOChildRequestAdd
):
    await RecordOTOService(db).add_one_child_record(record_child_data)
    await db.commit()
    return {"status": "ok"}


@router.put("/child_record/{record_child_id}")
async def edit_child_oto_record(
        db: DBDep,
        record_child_id: int,
        record_child_data: RecordOTOChildRequestAdd
):
    await RecordOTOService(db).edit_child_record(record_child_data=record_child_data, record_child_id=record_child_id)
    await db.commit()

    return {"status": "ok"}


@router.delete("/child_record/{record_child_id}")
async def delete_child_oto_record(
        db: DBDep,
        record_child_id: int
):
    await RecordOTOService(db).delete_child_oto_record(record_child_id)
    await db.commit()

    return {"status": "ok"}

