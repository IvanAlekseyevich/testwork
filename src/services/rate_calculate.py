from datetime import date

from src.db import rate_repository


async def calculate_price(cargo_id: int, date: date, price: float) -> int:
    rate = await rate_repository.get_earliest_date_rate(cargo_id, date)
    final_price = price + price * rate
    return final_price
