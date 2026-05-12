from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import insert, select, delete, update
from sqlalchemy.orm import selectinload

from src.models.students import StudentsOrm, StudentsTeachersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import StudentTeacherJoinDataMapper




class StudentsRepository(BaseRepository):
    model = StudentsOrm

    async def get_student_with_teachers(self, student_ids: list[UUID]):
        query = (
            select(self.model)
            .options(selectinload(self.model.teachers))
            .filter(StudentsOrm.id.in_(student_ids), self.model.is_deleted.is_(False))
        )

        result = await self.session.execute(query)
        model = result.scalars().all()

        return [student for student in model]

    async def create(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model.id, self.model.name, self.model.lastname)
        result = await self.session.execute(stmt)

        model = result.mappings().one()

        return model

class StudentsTeachersRepository(BaseRepository):
    model = StudentsTeachersOrm
    mapper = StudentTeacherJoinDataMapper

    async def create(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump())
        await self.session.execute(stmt)

    async def delete_by_fks(self, students_ids: list[UUID], teachers_ids: list[UUID]):
        if students_ids == [None] or students_ids == []:
            pass
        else:
            stmt_students = delete(self.model).filter(self.model.student_id.in_(students_ids))
            await self.session.execute(stmt_students)

        if teachers_ids == [None] or teachers_ids == []:
            pass
        else:
            stmt_teachers = update(self.model).filter(self.model.teacher_id.in_(teachers_ids)).values(is_deleted=False)
            await self.session.execute(stmt_teachers)


