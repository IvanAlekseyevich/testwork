from fastapi import APIRouter

from src import schemas

router_calculate = APIRouter(prefix="/calculate", tags=["calculate"])


@router_calculate.post(
    "/",
    response_model=int,
    status_code=201,
    summary="Returns the cost of cargo insurance on the specified date.",
)
async def update_rate(
        rates: schemas.CostOfInsurance,
) -> int:
    '''
    Aallows the user to obtain the cost of cargo insurance as of a certain date.
    '''
    pass
