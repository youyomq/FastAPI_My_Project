from uuid import UUID

from fastapi import APIRouter, Query

from src.schemas.answers import StatusOk, StatusOkWithData
from src.schemas.teachers import TeacherRequestAdd
from src.services.students_teachers import StudentTeacherService
from src.schemas.students_teachers import StudentTeacherRequestAdd
from src.core.dependencies import DBDep

router = APIRouter(prefix="/students_teachers", tags=["Students Teachers MTM Relationship"])

@router.get("/", response_model=StatusOkWithData)
async def get_students_teachers(
        db: DBDep,
        students_ids: list[UUID] = Query(default=None),
        teachers_ids: list[UUID] = Query(default=None)
):
    students_teachers = await StudentTeacherService(db).get_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)

    return {"status": "ok", "data": students_teachers}


@router.post("/", response_model=StatusOk)
async def add_student_teacher(
        db: DBDep,
        student_teacher_data: StudentTeacherRequestAdd
):
    await StudentTeacherService(db).add_student_teacher(student_teacher_data)
    await db.commit()

    return {"status": "ok"}


#@router.put("/{record_parent_id}", response_model=StatusOk)
#async def edit_student_teachers(
#        db: DBDep,
#        record_parent_id: UUID,
#        student_teacher_data: StudentTeacherRequestAdd
#):
#    await StudentTeacherService(db).edit_student_teacher(student_teacher_data=student_teacher_data, record_parent_id=record_parent_id)
#    await db.commit()
#
#    return {"status": "ok"}

#@router.delete("/{student_id}", response_model=StatusOk)
#async def delete_student_teachers(
#        db: DBDep,
#        students_ids: list[UUID],
#        teachers_ids: list[UUID]
#):
#    await StudentTeacherService(db).delete_students_teachers(students_ids=students_ids, teachers_ids=teachers_ids)
#    await db.commit()
#
#    return {"status": "ok"}






