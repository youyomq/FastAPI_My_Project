import typing

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if typing.TYPE_CHECKING:
    from src.models.records_otm_parent import RecordsOTMParentOrm

class RecordsOTMChildOrm(Base):
    __tablename__ = "records_otm_child"

    id: Mapped[int] = mapped_column(primary_key=True)
    child_value: Mapped[str] = mapped_column(String())
    parent_values: Mapped[list["RecordsOTMParentOrm"]] = relationship(
        back_populates="child_values",
        secondary="records_otm_parent_child"
    )


class RecordsOTMParentChildOrm(Base):
    __tablename__ = "records_otm_parent_child"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("records_otm_parent.id"))
    child_id: Mapped[int] = mapped_column(ForeignKey("records_otm_child.id"))