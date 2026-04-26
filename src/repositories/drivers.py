from src.models.drivers import DriversOrm
from src.repositories.mappers.mappers import DriverDataMapper
from src.repositories.base import BaseRepository

class DriversRepository(BaseRepository):
    model = DriversOrm
    mapper = DriverDataMapper
