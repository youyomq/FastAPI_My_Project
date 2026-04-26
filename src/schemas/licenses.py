from datetime import date
from uuid import UUID
from pydantic import BaseModel


class LicenseRequestAdd(BaseModel):
    license_number: str
    category: str
    date_issue: date

class LicenseRequestWithDateEndAdd(BaseModel):
    license_number: str
    category: str
    date_issue: date
    date_end: date

class LicenseAdd(BaseModel):
    id: UUID
    license_number: str
    category: str
    date_issue: date
    date_end: date

