import uuid
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    username: Mapped[str] = mapped_column(sa.String())