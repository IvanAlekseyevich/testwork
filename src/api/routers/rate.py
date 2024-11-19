from fastapi import APIRouter
from src import schemas
from src.db import cargo_repository, rate_repository
from datetime import date
router_rate = APIRouter(prefix="/rate", tags=["rate"])


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from pydantic import BaseModel, RootModel

class Cargo(BaseModel):
    cargo_type: str
    rate: str

class CargoData(RootModel):
    root: Dict[date, List[Cargo]]

# @app.post("/cargo-data/")
# async def receive_cargo_data(data: CargoData):
#     return {"received_data": data}

# Для запуска приложения:
# if __name__ == "__main__":
#     import uvicorn



@router_rate.post(
    "/",
    response_model=None,
    status_code=201,
    summary="Loading insurance rates by cargo type.",
)
async def load_insurance_rates(rates: CargoData) -> None:
    '''
    Allows you to upload cargo rates to the user.
    '''
    if not rates:
        return
    for start_date in rates:
        for date, cargo_dates in start_date[1].items():
            for cargo_data in cargo_dates:
                cargo_type = await cargo_repository.get_or_create(cargo_data.cargo_type)
                await rate_repository.create_or_update(
                    cargo_id=cargo_type.cargo_id,
                    date=date,
                    rate=cargo_data.rate)
