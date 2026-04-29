from src.repositories.orders import OrdersRepository
from src.repositories.customers import CustomersRepository
from src.repositories.teachers import TeachersRepository
from src.repositories.students import StudentsRepository, StudentsTeachersRepository
from src.repositories.licenses import LicensesRepository
from src.repositories.drivers import DriversRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.drivers = DriversRepository(self.session)
        self.licenses = LicensesRepository(self.session)
        self.customers = CustomersRepository(self.session)
        self.orders = OrdersRepository(self.session)
        self.teachers = TeachersRepository(self.session)
        self.students = StudentsRepository(self.session)
        self.students_teachers = StudentsTeachersRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()