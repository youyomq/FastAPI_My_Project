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