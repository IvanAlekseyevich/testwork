from datetime import date

from pydantic import BaseModel


class Cargo(BaseModel):
    cargo_type: str
    rate: float


class CargoData(RootModel):
    root: Dict[date, List[Cargo]]
