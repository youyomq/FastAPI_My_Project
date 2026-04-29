from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import insert, select, delete
from sqlalchemy.orm import selectinload

from src.models.students import StudentsOrm, StudentsTeachersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import StudentDataMapper, StudentTeacherJoinDataMapper




class StudentsRepository(BaseRepository):
    model = StudentsOrm
    mapper = StudentDataMapper

    async def get_student_with_teachers(self, student_ids: list[UUID]):
        query = (
            select(self.model)
            .options(selectinload(self.model.teachers))
            .filter(StudentsOrm.id.in_(student_ids))
        )

        result = await self.session.execute(query)
        model = result.scalars().all()

        return [student for student in model]

    async def add(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model.id, self.model.name, self.model.lastname)
        result = await self.session.execute(stmt)

        model = result.mappings().one()

        return model

class StudentsTeachersRepository(BaseRepository):
    model = StudentsTeachersOrm
    mapper = StudentTeacherJoinDataMapper

    async def add(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump())
        await self.session.execute(stmt)

    async def  delete_by_fks(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        if students_ids:
            stmt_students = delete(self.model).filter(self.model.student_id.in_(students_ids))
            await self.session.execute(stmt_students)

        if teachers_ids:
            stmt_teachers = delete(self.model).filter(self.model.teacher_id.in_(teachers_ids))
            await self.session.execute(stmt_teachers)


