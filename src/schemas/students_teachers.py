from uuid import UUID
from pydantic import BaseModel, ConfigDict

from src.schemas.students import Student, StudentCreateRequest, StudentCreate, Students
from src.schemas.teachers import TeacherCreateRequest, TeacherCreate, Teacher, Teachers


class StudentTeacherCreateRequest(BaseModel):
    student: StudentCreateRequest
    teacher: TeacherCreateRequest


class StudentTeacherCreate(BaseModel):
    student: StudentCreate
    teacher: TeacherCreate


class StudentTeacher(BaseModel):
    student: Student
    teacher: Teacher

class StudentsTeachers(BaseModel):
    students: Students
    teachers: Teachers

class StudentTeacherJoinCreateRequest(BaseModel):
    student_id: UUID
    teacher_id: UUID

class StudentTeacherJoinCreate(BaseModel):
    student_id: UUID
    teacher_id: UUID

class StudentTeacherListsJoinCreate(BaseModel):
    student: Student
    teacher: Teacher
    students_teachers: list[StudentTeacherJoinCreate]


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

