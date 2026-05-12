from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.schemas.students import Student


class TeacherCreateRequest(BaseModel):
    name: str
    lastname: str
    subject: str

    students: list[UUID] = []


class TeacherCreate(BaseModel):
    name: str
    lastname: str
    subject: str


class Teacher(TeacherCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class Teachers(BaseModel):
    teachers: list[Teacher]



