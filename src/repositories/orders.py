from src.models.orders import OrdersOrm
from src.repositories.mappers.mappers import OrderDataMapper
from src.repositories.base import BaseRepository


class OrdersRepository(BaseRepository):
    model = OrdersOrm
    mapper = OrderDataMapper