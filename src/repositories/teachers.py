from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from src.models.teachers import TeachersOrm
from src.repositories.base import BaseRepository


class TeachersRepository(BaseRepository):
    model = TeachersOrm

    async def get_teacher_with_students(self, teachers_ids: list[UUID]):
        query = (
            select(self.model)
            .options(selectinload(self.model.students))
            .filter(self.model.id.in_(teachers_ids), self.model.is_deleted.is_(False))
        )

        result = await self.session.execute(query)
        model = result.scalars().all()

        return [teacher for teacher in model]

    async def create(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(TeachersOrm.id,
                                                                        TeachersOrm.name,
                                                                        TeachersOrm.lastname,
                                                                        TeachersOrm.subject
                                                                        )
        result = await self.session.execute(stmt)

        model = result.mappings().one()

        return model
