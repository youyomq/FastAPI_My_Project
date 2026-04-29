from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.schemas.students import Student


class TeacherRequestAdd(BaseModel):
    name: str
    lastname: str
    subject: str

    students: list[UUID] = []


class TeacherAdd(BaseModel):
    name: str
    lastname: str
    subject: str



class Teacher(TeacherAdd):
    id: UUID


