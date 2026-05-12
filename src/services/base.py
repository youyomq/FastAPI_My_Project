from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import DBDep


class BaseService:
    db: DBDep | None

    def __init__(self, db: DBDep | None = None) -> None:
        self.db = db