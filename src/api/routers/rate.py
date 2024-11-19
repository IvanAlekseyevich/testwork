from fastapi import APIRouter

from src import schemas
from src.db import cargo_repository, rate_repository

router_rate = APIRouter(prefix="/rate", tags=["rate"])


@router_rate.post(
    "/",
    response_model=None,
    status_code=201,
    summary="Loading insurance rates by cargo type.",
)
async def load_insurance_rates(rates: schemas.CargoData) -> None:
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
