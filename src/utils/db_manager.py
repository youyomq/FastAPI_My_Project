from src.repositories.records_otm_parent import RecordsOTMParentRepository
from src.repositories.records_otm_child import RecordsOTMChildRepository, RecordsOTMParentChildRepository
from src.repositories.records_oto_child import RecordsOTOChildRepository
from src.repositories.records_oto_parent import RecordsOTOParentRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.records_oto_parent = RecordsOTOParentRepository(self.session)
        self.records_oto_child = RecordsOTOChildRepository(self.session)
        self.records_otm_parent = RecordsOTMParentRepository(self.session)
        self.records_otm_child = RecordsOTMChildRepository(self.session)
        self.records_otm_parent_child = RecordsOTMParentChildRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()