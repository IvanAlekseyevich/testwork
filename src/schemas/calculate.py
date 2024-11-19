# from .base import DBObjectBase
from datetime import date
from pydantic import BaseModel

# class CargoTypeAndTimeRequest(DBObjectBase):
#     id: int
#     company_name: str
#     client_industry: str
#     software_stack: str
#     industry_choice: str
#     contact_marketing: str
#     owner_id: int
#     logo: str


class CostOfInsurance(BaseModel):
    cargo_type: str
    date: date
    price: float
