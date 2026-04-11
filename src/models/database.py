import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeMeta, Mapped, declarative_base, mapped_column

from src.config import settings

engine=create_async_engine(str(settings.postgres_url))
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


metadata = sa.MetaData()


class BaseServiceModel:
    """Базовый класс для таблиц сервиса."""

    @classmethod
    def on_conflict_constraint(cls) -> tuple | None:
        return None


Base: DeclarativeMeta = declarative_base(metadata=metadata, cls=BaseServiceModel)


