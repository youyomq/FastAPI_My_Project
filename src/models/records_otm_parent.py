import typing

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if typing.TYPE_CHECKING:
    from src.models.records_otm_child import RecordsOTMChildOrm

class RecordsOTMParentOrm(Base):
    __tablename__ = "records_otm_parent"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_value: Mapped[str] = mapped_column(String(length=100))

    child_values: Mapped[list["RecordsOTMChildOrm"]] = relationship(
        secondary="records_otm_parent_child"
    )