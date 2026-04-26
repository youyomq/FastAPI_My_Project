from uuid import UUID, uuid4

from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.database import Base

class LicensesOrm(Base):
    __tablename__ = "licenses"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    license_number: Mapped[str] = mapped_column(String(length=100))
    category: Mapped[str] = mapped_column(String(length=5))
    date_issue: Mapped[date] = mapped_column(default=date.today())
    date_end: Mapped[date] = mapped_column()
