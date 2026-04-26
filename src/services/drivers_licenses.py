from datetime import date

from uuid import UUID

from src.schemas.licenses import LicenseAdd, LicenseRequestWithDateEndAdd
from src.schemas.drivers_licenses import DriverLicenseRequestAdd, DriverLicense
from src.schemas.drivers import DriverAdd, DriverRequestAdd
from src.services.base import BaseService
from utils.date import get_end_date


class DriverLicenseService(BaseService):
    async def get_one_driver_license(self, driver_id: UUID):
        driver = await self.db.drivers.get_one_or_none(id=driver_id)
        license_ = await self.db.licenses.get_one_or_none(id=driver.license_id)

        res_record = DriverLicense(driver=driver.model_dump(), license=license_.model_dump())
        return res_record


    async def add_one_driver_license(self, driver_license_data: DriverLicenseRequestAdd):
        date_end = get_end_date(driver_license_data.license.date_issue)
        license_data =  LicenseRequestWithDateEndAdd(**driver_license_data.license.model_dump(), date_end=date_end)
        added_license = await self.db.licenses.add_one(data=license_data)

        driver_data = DriverAdd(
            name=driver_license_data.driver.name,
            lastname=driver_license_data.driver.lastname,
            license_id=added_license.id
        )

        await self.db.drivers.add_one(data=driver_data)


    async def edit_driver_license(self, driver_id: UUID, driver_license_data:DriverLicenseRequestAdd):
        date_end = get_end_date(driver_license_data.license.date_issue)
        driver_updated = await self.db.drivers.edit_one(data=driver_license_data.driver, id=driver_id)
        license_data = LicenseRequestWithDateEndAdd(**driver_license_data.license.model_dump(), date_end=date_end)

        await self.db.licenses.edit_one(data=license_data, id=driver_updated.license_id)


    async def delete_driver_license(self, driver_id: UUID):
        deleted_driver = await self.db.drivers.delete(id=driver_id)
        await self.db.licenses.delete(id=deleted_driver.license_id)


