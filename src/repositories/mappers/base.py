from pydantic import BaseModel

from src.models.database import Base

class DataMapper:
    db_model: type[Base] = None
    schema: type[BaseModel] = None

    @classmethod
    def map_to_domain_entity(cls, data):
        return cls.schema.model_validate(
            data, from_attributes=True
        )

    @classmethod
    def map_to_persistence_entity(cls):
        return cls.db_model(
            **cls.schema.model_dump()
        )
