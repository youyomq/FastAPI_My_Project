import typing
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if typing.TYPE_CHECKING:
    from src.models.students import StudentsOrm

class TeachersOrm(Base):
    __tablename__ = "teachers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    name: Mapped[str] = mapped_column(String(length=100))
    lastname: Mapped[str] = mapped_column(String(length=100))
    subject: Mapped[str] = mapped_column(String(length=100))
    
    students: Mapped[list["StudentsOrm"]] = relationship(
        back_populates="teachers",
        secondary="students_teachers",
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    is_deleted: Mapped[bool] = mapped_column(default=False)