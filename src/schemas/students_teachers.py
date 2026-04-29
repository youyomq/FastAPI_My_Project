from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

from src.schemas.students import Student, StudentRequestAdd, StudentAdd
from src.schemas.teachers import TeacherRequestAdd, TeacherAdd, Teacher


class StudentTeacherRequestAdd(BaseModel):
    student: StudentRequestAdd
    teacher: TeacherRequestAdd


class StudentTeacherAdd(BaseModel):
    student: StudentAdd
    teacher: TeacherAdd


class StudentTeacher(BaseModel):
    student: Student
    teacher: Teacher


class StudentTeacherJoinRequestAdd(BaseModel):
    student_id: UUID
    teacher_id: UUID

class StudentTeacherJoinAdd(BaseModel):
    student_id: UUID
    teacher_id: UUID

class StudentTeacherJoin(BaseModel):
    id: UUID
    student_id: UUID
    teacher_id: UUID

    model_config = ConfigDict(from_attributes=True)

class StudentWithTeachers(BaseModel):
    id: UUID
    name: str
    lastname: str
    teachers: list[Teacher]

class TeacherWithStudents(BaseModel):
    name: str
    lastname: str
    subject: str
    students: list[Student]

class StudentsWithTeachersLists(BaseModel):
    students: list[StudentWithTeachers] | None = None
    teachers: list[TeacherWithStudents] | None = None

