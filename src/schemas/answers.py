from pydantic import BaseModel


class StatusOk:
    @classmethod
    def answer_ok(cls):
        return {"status": "ok"}


class StatusOkWithData:
    def __init__(self, data: BaseModel):
        self.data = data

    def answer_ok(self):
        return {"status": "ok", "data": self.data}