from uuid import UUID, uuid4

from src.models.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class RecordsOTMParentOrm(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id"))
    order_article: Mapped[str] = mapped_column(String(20))