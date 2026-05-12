from uuid import UUID

from fastapi import APIRouter, Query

from src.services.students_teachers import StudentTeacherService
from src.schemas.students_teachers import StudentTeacherCreateRequest, StudentsWithTeachersLists, StudentTeacher, \
    StudentTeacherListsJoinCreate, StudentsTeachers
from src.dependencies import DBDep

router = APIRouter(prefix="/students_teachers", tags=["Students Teachers MTM Relationship"])

@router.get("/", response_model=StudentsWithTeachersLists)
async def get_students_teachers(
        db: DBDep,
        students_ids: list[UUID] = Query(default=[]),
        teachers_ids: list[UUID] = Query(default=[])
):
    return await StudentTeacherService(db).get_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)


@router.post("/", response_model=StudentTeacherListsJoinCreate, status_code=201)
async def create_student_teacher(
        db: DBDep,
        student_teacher_data: StudentTeacherCreateRequest
):
    return await StudentTeacherService(db).create_student_teacher(student_teacher_data)


@router.put("/", response_model=StudentTeacherListsJoinCreate, status_code=200)
async def edit_student_teachers(
        db: DBDep,
        student_teacher_data: StudentTeacherCreateRequest,
        teacher_id: UUID = Query(),
        student_id: UUID = Query()
):
    return await StudentTeacherService(db).edit_student_teacher(student_teacher_data=student_teacher_data, teacher_id=teacher_id, student_id=student_id)


@router.delete("/", response_model=StudentsTeachers, status_code=200)
async def delete_student_teachers(
        db: DBDep,
        students_ids: list[UUID] = Query(default=[]),
        teachers_ids: list[UUID] = Query(default=[])
):
    return await StudentTeacherService(db).delete_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)






