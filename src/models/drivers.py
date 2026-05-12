from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class DriversOrm(Base):
    __tablename__ = "drivers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str] = mapped_column(String(length=100))
    lastname: Mapped[str] = mapped_column(String(length=100))

    license_id: Mapped[UUID] = mapped_column(
        ForeignKey("licenses.id"),
        unique=True
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    is_deleted: Mapped[bool] = mapped_column(default=False)