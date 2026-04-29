from datetime import date

from uuid import UUID

from repositories.mappers.mappers import DriverDataMapper, LicenseDataMapper
from src.schemas.licenses import LicenseAdd, LicenseRequestWithDateEndAdd
from src.schemas.drivers_licenses import DriverLicenseRequestAdd, DriverLicense
from src.schemas.drivers import DriverAdd, DriverRequestAdd
from src.services.base import BaseService
from utils.date import get_end_date


class DriverLicenseService(BaseService):
    async def get_one_driver_license(self, driver_id: UUID):
        driver_model = await self.db.drivers.get_one_or_none(id=driver_id)
        driver = DriverDataMapper.map_to_domain_entity(driver_model)

        license_model = await self.db.licenses.get_one_or_none(id=driver.license_id)
        license_ = LicenseDataMapper.map_to_domain_entity(license_model)

        res_record = DriverLicense(driver=driver.model_dump(), license=license_.model_dump())
        return res_record


    async def add_driver_license(self, driver_license_data: DriverLicenseRequestAdd):
        date_end = get_end_date(driver_license_data.license.date_issue)

        license_data = LicenseRequestWithDateEndAdd(**driver_license_data.license.model_dump(), date_end=date_end)
        added_license_model = await self.db.licenses.add(data=license_data)
        added_license = LicenseDataMapper.map_to_domain_entity(added_license_model)

        driver_data = DriverAdd(
            name=driver_license_data.driver.name,
            lastname=driver_license_data.driver.lastname,
            license_id=added_license.id
        )

        await self.db.drivers.add(data=driver_data)


    async def edit_driver_license(self, driver_id: UUID, driver_license_data:DriverLicenseRequestAdd):
        date_end = get_end_date(driver_license_data.license.date_issue)

        driver_updated_model = await self.db.drivers.edit_one(data=driver_license_data.driver, id=driver_id)
        driver_updated = DriverDataMapper.map_to_domain_entity(driver_updated_model)
        license_data = LicenseRequestWithDateEndAdd(**driver_license_data.license.model_dump(), date_end=date_end)

        await self.db.licenses.edit_one(data=license_data, id=driver_updated.license_id)


    async def delete_driver_license(self, driver_id: UUID):
        deleted_driver_model = await self.db.drivers.delete(id=driver_id)
        deleted_driver = DriverDataMapper.map_to_domain_entity(deleted_driver_model)

        await self.db.licenses.delete(id=deleted_driver.license_id)


