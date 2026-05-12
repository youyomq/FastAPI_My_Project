import typing
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if typing.TYPE_CHECKING:
    from src.models.teachers import TeachersOrm

class StudentsOrm(Base):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(length=100))
    lastname: Mapped[str] = mapped_column(String(length=100))
 
    teachers: Mapped[list["TeachersOrm"]] = relationship(
        back_populates="students",
        secondary="students_teachers",
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    is_deleted: Mapped[bool] = mapped_column(default=False)


class StudentsTeachersOrm(Base):
    __tablename__ = "students_teachers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey("teachers.id", ondelete="CASCADE"))
    student_id: Mapped[UUID] = mapped_column(ForeignKey("students.id", ondelete="CASCADE"))

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    is_deleted: Mapped[bool] = mapped_column(default=False)