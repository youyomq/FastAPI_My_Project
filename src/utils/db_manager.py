from src.repositories.records_otm_parent import RecordsOTMParentRepository
from src.repositories.records_otm_child import RecordsOTMChildRepository
from src.repositories.records_mtm_parent import RecordsMTMParentRepository
from src.repositories.records_mtm_child import RecordsMTMChildRepository, RecordsMTMParentChildRepository
from src.repositories.records_oto_child import RecordsOTOChildRepository
from src.repositories.records_oto_parent import RecordsOTOParentRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.records_oto_parent = RecordsOTOParentRepository(self.session)
        self.records_oto_child = RecordsOTOChildRepository(self.session)
        self.records_otm_child = RecordsOTMChildRepository(self.session)
        self.records_otm_parent = RecordsOTMParentRepository(self.session)
        self.records_mtm_parent = RecordsMTMParentRepository(self.session)
        self.records_mtm_child = RecordsMTMChildRepository(self.session)
        self.records_mtm_parent_child = RecordsMTMParentChildRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()