import datetime

class BaseProjectException(Exception):
    pass


class CargoCantCreateError(BaseProjectException):
    def __init__(self, cargo_type: str) -> None:
        self.cargo_type = cargo_type
        super().__init__(f"Невозможно создать cargo_type={self.cargo_type}.")


class RateCantCreateError(BaseProjectException):
    def __init__(self, cargo_id: int, date: datetime.date, rate: float) -> None:
        self.cargo_id = cargo_id
        self.date = date
        self.rate = rate
        super().__init__(f"Невозможно создать cargo_id={self.cargo_id}, date={self.date}, rate={self.rate}.")
