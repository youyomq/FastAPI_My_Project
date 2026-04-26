from pydantic import BaseModel


class StatusOk(BaseModel):
    status: str = "ok"

class StatusOkWithData(BaseModel):
    status: str = "ok"
    data: BaseModel