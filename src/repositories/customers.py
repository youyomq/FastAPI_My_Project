from src.models.customers import CustomersOrm
from src.repositories.base import BaseRepository


class CustomersRepository(BaseRepository):
    model = CustomersOrm
