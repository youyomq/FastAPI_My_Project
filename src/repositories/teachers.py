from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm import selectinload


from src.models.students import StudentsTeachersOrm
from src.repositories.students import StudentsTeachersRepository
from src.schemas.students import StudentTeacherAdd
from src.schemas.teachers import TeacherRequestAdd, TeacherAdd
from src.models.teachers import TeachersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import TeacherDataMapper, StudentTeacherJoinDataMapper


class TeachersRepository(BaseRepository):
    model = TeachersOrm
    mapper = TeacherDataMapper

    async def get_teacher_with_students(self, teachers_ids: list[UUID]):
        query = (
            select(self.model)
            .options(selectinload(self.model.students))
            .filter(self.model.id.in_(teachers_ids))
        )

        result = await self.session.execute(query)
        model = result.scalars().all()

        return [teacher for teacher in model]

    async def add(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(TeachersOrm.id,
                                                                        TeachersOrm.name,
                                                                        TeachersOrm.lastname,
                                                                        TeachersOrm.subject
                                                                        )
        result = await self.session.execute(stmt)

        model = result.mappings().one()

        return self.mapper.map_to_domain_entity(model)
