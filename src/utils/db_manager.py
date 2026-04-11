from repositories.records_child import RecordsChildRepository
from repositories.records_parent import RecordsParentRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.records_parent = RecordsParentRepository(self.session)
        self.records_child = RecordsChildRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()