from uuid import UUID

from pydantic import BaseModel, ConfigDict


class StudentCreateRequest(BaseModel):
    name: str
    lastname: str

    teachers: list[UUID] = []


class StudentCreate(BaseModel):
    name: str
    lastname: str


class Student(StudentCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class Students(BaseModel):
    students: list[Student]


class StudentTeacherCreate(BaseModel):
    teacher_id: UUID
    student_id: UUID

class StudentTeacher(StudentTeacherCreate):
    id: UUID

