from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session


DBDep = Annotated[
    AsyncSession, Depends(get_session)
]