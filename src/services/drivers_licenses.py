from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.drivers import DriversRepository
from repositories.licenses import LicensesRepository
from schemas.drivers import Driver
from src.schemas.licenses import LicenseRequestWithDateEndCreate, License
from src.schemas.drivers_licenses import DriverLicenseCreateRequest, DriverLicense
from src.schemas.drivers import DriverCreate
from src.services.base import BaseService
from utils.date import get_end_date


class DriverLicenseService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(db)
        self.drivers_repository = DriversRepository(db)
        self.licenses_repository = LicensesRepository(db)

    async def get_one_driver_license(self, driver_id: UUID):
        driver_model = await self.drivers_repository.get_one_or_none(id=driver_id)
        driver = Driver.model_validate(driver_model, from_attributes=True)

        license_model = await self.licenses_repository.get_one_or_none(id=driver.license_id)
        license_ = License.model_validate(license_model, from_attributes=True)

        res_record = DriverLicense(driver=driver.model_dump(), license=license_.model_dump())

        await self.db.commit()
        return res_record


    async def create_driver_license(self, driver_license_data: DriverLicenseCreateRequest):
        date_end = get_end_date(driver_license_data.license.date_issue)

        license_data = LicenseRequestWithDateEndCreate(**driver_license_data.license.model_dump(), date_end=date_end)
        created_license_model = await self.licenses_repository.create(data=license_data)
        created_license = License.model_validate(created_license_model, from_attributes=True)

        driver_data = DriverCreate(
            name=driver_license_data.driver.name,
            lastname=driver_license_data.driver.lastname,
            license_id=created_license.id
        )

        created_driver_model = await self.drivers_repository.create(data=driver_data)
        created_driver = Driver.model_validate(created_driver_model, from_attributes=True)

        created_driver_license = DriverLicense(driver=created_driver.model_dump(), license=created_license.model_dump())

        await self.db.commit()

        return created_driver_license

    async def edit_driver_license(self, driver_id: UUID, driver_license_data:DriverLicenseCreateRequest):
        date_end = get_end_date(driver_license_data.license.date_issue)

        driver_updated_model = await self.drivers_repository.edit_one(data=driver_license_data.driver, id=driver_id)
        driver_updated = Driver.model_validate(driver_updated_model, from_attributes=True)
        license_data = LicenseRequestWithDateEndCreate(**driver_license_data.license.model_dump(), date_end=date_end)

        license_updated_model = await self.licenses_repository.edit_one(data=license_data, id=driver_updated.license_id)
        license_update = License.model_validate(license_updated_model, from_attributes=True)

        updated_driver_license = DriverLicense(driver=driver_updated.model_dump(), license=license_update.model_dump())

        await self.db.commit()

        return updated_driver_license

    async def delete_driver_license(self, driver_id: UUID):
        deleted_driver_model = await self.drivers_repository.delete(id=driver_id)
        deleted_driver = Driver.model_validate(deleted_driver_model, from_attributes=True)

        deleted_license_model = await self.licenses_repository.delete(id=deleted_driver.license_id)
        deleted_license = License.model_validate(deleted_license_model, from_attributes=True)

        deleted_driver_license = DriverLicense(driver=deleted_driver.model_dump(), license=deleted_license.model_dump())

        await self.db.commit()

        return deleted_driver_license


