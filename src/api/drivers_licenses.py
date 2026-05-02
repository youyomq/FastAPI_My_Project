from uuid import UUID

from fastapi import APIRouter

from src.schemas.answers import StatusOk, StatusOkWithData
from src.schemas.drivers_licenses import DriverLicenseRequestAdd, DriverLicense
from src.dependencies import DBDep
from src.services.drivers_licenses import DriverLicenseService


router = APIRouter(prefix="/driver_license", tags=["Driver License OTO Relationship"])

@router.get("/{driver_id}", response_model=StatusOkWithData[DriverLicense])
async def get_one_driver_license(
        db: DBDep,
        driver_id: UUID
):
    driver_license = await DriverLicenseService(db).get_one_driver_license(driver_id)

    return driver_license


@router.post("/", response_model=StatusOk, status_code=201)
async def add_driver_license(
        db: DBDep,
        driver_license_data: DriverLicenseRequestAdd
):
    await DriverLicenseService(db).add_driver_license(driver_license_data=driver_license_data)
    await db.commit()

    return {"status": "ok"}


@router.put("/{driver_id}", response_model=StatusOk)
async def edit_driver_license(
        db: DBDep,
        driver_id: UUID,
        driver_license_data: DriverLicenseRequestAdd
):
    await DriverLicenseService(db).edit_driver_license(driver_id=driver_id, driver_license_data=driver_license_data)
    await db.commit()

    return {"status": "ok"}



@router.delete("/{driver_id}", status_code=204)
async def delete_driver_license(
        db: DBDep,
        driver_id: UUID
):
    await DriverLicenseService(db).delete_driver_license(driver_id)
    await db.commit()










