import typing
from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if typing.TYPE_CHECKING:
    from src.models.records_mtm_child import RecordsMTMChildOrm

class RecordsMTMParentOrm(Base):
    __tablename__ = "records_mtm_parent"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    parent_value: Mapped[str] = mapped_column(String(length=100))

    child_values: Mapped[list["RecordsMTMChildOrm"]] = relationship(
        back_populates="parent_values",
        secondary="records_mtm_parent_child"
    )