from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

class CustomersOrm(Base):
    __tablename__ = "customers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    name: Mapped[str] = mapped_column(String(length=50), unique=True)

    orders = relationship(
        "OrdersOrm",
        back_populates="customer",
        cascade="save-update, merge, delete"
    )