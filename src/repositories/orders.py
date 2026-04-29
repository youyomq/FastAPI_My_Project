from src.models.orders import OrdersOrm
from src.repositories.base import BaseRepository


class OrdersRepository(BaseRepository):
    model = OrdersOrm