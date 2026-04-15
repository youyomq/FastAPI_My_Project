from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.database import Base


class RecordsOTOParentOrm(Base):
    __tablename__ = "records_oto_parent"

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_id: Mapped[int] = mapped_column(ForeignKey("records_oto_child.id"), unique=True)
    parent_value: Mapped[str] = mapped_column(String(length=100))