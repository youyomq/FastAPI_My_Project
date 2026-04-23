from uuid import UUID, uuid4

from src.models.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, MapperEvents


class RecordsOTMParentOrm(Base):
    __tablename__ = "records_otm_parent"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    parent_id: Mapped[UUID] = mapped_column(default=uuid4)
    parent_value: Mapped[str] = mapped_column(String())
    fk_id: Mapped[UUID] = mapped_column(ForeignKey("records_otm_child.id"))