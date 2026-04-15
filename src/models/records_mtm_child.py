import typing

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if typing.TYPE_CHECKING:
    from src.models.records_mtm_parent import RecordsMTMParentOrm

class RecordsMTMChildOrm(Base):
    __tablename__ = "records_mtm_child"

    id: Mapped[int] = mapped_column(primary_key=True)
    child_value: Mapped[str] = mapped_column(String())
    parent_values: Mapped[list["RecordsMTMParentOrm"]] = relationship(
        back_populates="child_values",
        secondary="records_mtm_parent_child"
    )


class RecordsMTMParentChildOrm(Base):
    __tablename__ = "records_mtm_parent_child"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("records_mtm_parent.id"))
    child_id: Mapped[int] = mapped_column(ForeignKey("records_mtm_child.id"))