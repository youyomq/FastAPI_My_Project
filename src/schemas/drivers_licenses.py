from pydantic import BaseModel, ConfigDict

from schemas.licenses import LicenseCreate, LicenseCreateRequest, License
from schemas.drivers import DriverCreate, DriverCreateRequest, Driver


class DriverLicenseCreateRequest(BaseModel):
    driver: DriverCreateRequest
    license: LicenseCreateRequest


class DriverLicenseCreate(BaseModel):
    driver: DriverCreate
    license: LicenseCreate


class DriverLicense(DriverLicenseCreate):
    driver: Driver
    license: License
