from datetime import date

from pydantic import BaseModel


class CostOfInsurance(BaseModel):
    cargo_type: str
    date: date
    price: float
