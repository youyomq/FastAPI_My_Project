from pydantic import BaseModel, ConfigDict

from schemas.licenses import LicenseAdd, LicenseRequestAdd
from schemas.drivers import DriverAdd, DriverRequestAdd


class DriverLicenseRequestAdd(BaseModel):
    driver: DriverRequestAdd
    license: LicenseRequestAdd


class DriverLicenseAdd(BaseModel):
    driver: DriverAdd
    license: LicenseAdd


class DriverLicense(DriverLicenseAdd):
    model_config = ConfigDict(from_attributes=True)