from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.database import Base

class RecordsOTOChildOrm(Base):
    __tablename__ = "records_oto_child"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    child_value: Mapped[str] = mapped_column(String(length=100))

