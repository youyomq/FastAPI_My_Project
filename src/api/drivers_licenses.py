from uuid import UUID

from fastapi import APIRouter

from schemas.drivers_licenses import DriverLicense
from src.schemas.drivers_licenses import DriverLicenseCreateRequest
from src.dependencies import DBDep
from src.services.drivers_licenses import DriverLicenseService


router = APIRouter(prefix="/driver_license", tags=["Driver License OTO Relationship"])

@router.get("/{driver_id}", response_model=DriverLicense)
async def get_one_driver_license(
        db: DBDep,
        driver_id: UUID
):
    return await DriverLicenseService(db).get_one_driver_license(driver_id)


@router.post("/", response_model=DriverLicense, status_code=201)
async def create_driver_license(
        db: DBDep,
        driver_license_data: DriverLicenseCreateRequest
):
    return await DriverLicenseService(db).create_driver_license(driver_license_data=driver_license_data)


@router.put("/{driver_id}", response_model=DriverLicense, status_code=200)
async def edit_driver_license(
        db: DBDep,
        driver_id: UUID,
        driver_license_data: DriverLicenseCreateRequest
):
    return await DriverLicenseService(db).edit_driver_license(driver_id=driver_id, driver_license_data=driver_license_data)



@router.delete("/{driver_id}", response_model=DriverLicense, status_code=200)
async def delete_driver_license(
        db: DBDep,
        driver_id: UUID
):
    return await DriverLicenseService(db).delete_driver_license(driver_id)










