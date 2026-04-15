from src.models.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, MapperEvents


class RecordsOTMParentOrm(Base):
    __tablename__ = "records_otm_parent"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column()
    parent_value: Mapped[str] = mapped_column(String())
    fk_id: Mapped[int] = mapped_column(ForeignKey("records_otm_child.id"))