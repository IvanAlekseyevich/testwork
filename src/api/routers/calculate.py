from fastapi import APIRouter

from src import schemas
from src.db import cargo_repository
from src.services import calculate_price

router_calculate = APIRouter(prefix="/calculate", tags=["calculate"])


@router_calculate.post(
    "/",
    response_model=str,
    status_code=201,
    summary="Returns the cost of cargo insurance on the specified date.",
)
async def update_rate(
        data: schemas.CostOfInsurance,
) -> str:
    cargo = await cargo_repository.get(data.cargo_type)
    price = await calculate_price(cargo.id, data.date, float(data.price))
    return str(price)
