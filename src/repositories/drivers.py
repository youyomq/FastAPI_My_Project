from src.models.drivers import DriversOrm
from src.repositories.base import BaseRepository

class DriversRepository(BaseRepository):
    model = DriversOrm
