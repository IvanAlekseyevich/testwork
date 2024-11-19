from datetime import date

from pydantic import BaseModel, RootModel


class Cargo(BaseModel):
    cargo_type: str
    rate: float


class CargoData(RootModel):
    root: dict[date, list[Cargo]]
