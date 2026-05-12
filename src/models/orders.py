from datetime import datetime
from uuid import UUID, uuid4

from src.models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class OrdersOrm(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    order_article: Mapped[str] = mapped_column(String(20))
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)

    customer = relationship(
        "CustomersOrm",
        back_populates="orders"
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
    is_deleted: Mapped[bool] = mapped_column(default=False)