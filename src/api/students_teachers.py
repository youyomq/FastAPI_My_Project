from uuid import UUID

from fastapi import APIRouter, Query

from src.schemas.answers import StatusOk, StatusOkWithData
from src.services.students_teachers import StudentTeacherService
from src.schemas.students_teachers import StudentTeacherRequestAdd, StudentsWithTeachersLists
from src.dependencies import DBDep

router = APIRouter(prefix="/students_teachers", tags=["Students Teachers MTM Relationship"])

@router.get("/", response_model=StatusOkWithData[StudentsWithTeachersLists])
async def get_students_teachers(
        db: DBDep,
        students_ids: list[UUID] = Query(default=[]),
        teachers_ids: list[UUID] = Query(default=[])
):
    students_teachers = await StudentTeacherService(db).get_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)

    return StatusOkWithData(data=students_teachers)


@router.post("/", response_model=StatusOk, status_code=201)
async def add_student_teacher(
        db: DBDep,
        student_teacher_data: StudentTeacherRequestAdd
):
    await StudentTeacherService(db).add_student_teacher(student_teacher_data)
    await db.commit()

    return StatusOk()


@router.put("/", response_model=StatusOk)
async def edit_student_teachers(
        db: DBDep,
        student_teacher_data: StudentTeacherRequestAdd,
        teacher_id: UUID = Query(),
        student_id: UUID = Query()
):
    await StudentTeacherService(db).edit_student_teacher(student_teacher_data=student_teacher_data, teacher_id=teacher_id, student_id=student_id)
    await db.commit()

    return StatusOk()


@router.delete("/", status_code=204)
async def delete_student_teachers(
        db: DBDep,
        students_ids: list[UUID] = Query(default=[]),
        teachers_ids: list[UUID] = Query(default=[])
):
    await StudentTeacherService(db).delete_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)
    await db.commit()







