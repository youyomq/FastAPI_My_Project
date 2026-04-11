from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.database import Base

class RecordsChildOrm(Base):
    __tablename__ = "records_oto_child"

    id: Mapped[int] = mapped_column(primary_key=True)
    child_value: Mapped[str] = mapped_column(String(length=100))

