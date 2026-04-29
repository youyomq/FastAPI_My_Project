from uuid import UUID

from pydantic import BaseModel, ConfigDict


class StudentRequestAdd(BaseModel):
    name: str
    lastname: str

    teachers: list[UUID] = []


class StudentAdd(BaseModel):
    name: str
    lastname: str


class Student(StudentAdd):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class StudentTeacherAdd(BaseModel):
    teacher_id: UUID
    student_id: UUID

class StudentTeacher(StudentTeacherAdd):
    id: UUID

