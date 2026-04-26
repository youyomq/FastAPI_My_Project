from typing import Annotated

from fastapi import Depends

from src.db import SessionFactory
from src.utils.db_manager import DBManager


def get_db_manager():
    return DBManager(session_factory=SessionFactory)


async def get_db():
    async with get_db_manager() as db:
        yield db


DBDep = Annotated[
    DBManager, Depends(get_db)
]