from fastapi import APIRouter

from src.schemas.records_otm_parent import RecordOTMParentRequestAdd
from src.services.records_otm import RecordOTMService
from src.schemas.records_otm_child import RecordOTMChildRequestAdd
from src.api.dependencies import DBDep

router = APIRouter(prefix="/records_otm")

@router.get("/check_health")
async def check_health():
    return {"status": "ok"}

@router.get("/parent")
async def get_all_parent_otm_records(
        db: DBDep
):
    parent_records = await RecordOTMService(db).get_all_parent_otm_records()

    return {"status": "ok", "data": parent_records}


@router.post("/add_parent")
async def add_one_parent_otm_records(
        db: DBDep,
        record_parent_data: RecordOTMParentRequestAdd
):
    await RecordOTMService(db).add_one_parent_otm_record(record_parent_data)
    await db.commit()

    return {"status": "ok"}


@router.get("/child")
async def get_all_child_otm_records(
        db: DBDep
):
    child_records = await RecordOTMService(db).get_all_child_otm_records()

    return {"status": "ok", "data": child_records}

@router.post("/add_child")
async def add_one_child_otm_record(
        db: DBDep,
        record_child_data: RecordOTMChildRequestAdd
):
    await RecordOTMService(db).add_one_child_otm_record(record_child_data)
    await db.commit()
    return {"status": "ok"}


@router.put("/edit_child/{record_child_id}")
async def edit_child_otm_record(
        db: DBDep,
        record_child_id: int,
        record_child_data: RecordOTMChildRequestAdd
):
    await RecordOTMService(db).edit_child_otm_record(record_child_data=record_child_data, record_child_id=record_child_id)
    await db.commit()

    return {"status": "ok"}


@router.delete("/delete_child/{record_child_id}")
async def delete_child_otm_record(
        db: DBDep,
        record_child_id: int
):
    await RecordOTMService(db).delete_child_otm_record(record_child_id=record_child_id)
    await db.commit()

    return {"status": "ok"}



