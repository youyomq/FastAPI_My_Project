from datetime import date
from uuid import UUID
from pydantic import BaseModel


class LicenseCreateRequest(BaseModel):
    license_number: str
    category: str
    date_issue: date

class LicenseRequestWithDateEndCreate(BaseModel):
    license_number: str
    category: str
    date_issue: date
    date_end: date

class LicenseCreate(BaseModel):
    id: UUID
    license_number: str
    category: str
    date_issue: date
    date_end: date


class License(BaseModel):
    id: UUID
    license_number: str
    category: str
    date_issue: date
    date_end: date
