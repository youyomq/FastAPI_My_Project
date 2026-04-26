from src.models.customers import CustomersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import CustomerDataMapper


class CustomersRepository(BaseRepository):
    model = CustomersOrm
    mapper = CustomerDataMapper
