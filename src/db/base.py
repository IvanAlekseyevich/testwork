import datetime
from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src import exceptions
from src.db.models import Rate, Cargo
from src.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, model: T, session: AsyncSession) -> None:
        self._model = model
        self._session = session


class CargoRepository(BaseRepository[Cargo]):

    def __init__(self) -> None:
        super().__init__(Cargo, async_session())

    async def get_or_create(self, cargo_type: str) -> Cargo:
        instance = await self._session.scalar(select(Cargo).where(self._model.cargo_type == cargo_type))
        if instance:
            return instance
        try:
            instance = self._model.new_cargo(cargo_type=cargo_type)
            self._session.add(instance)
            await self._session.commit()
        except Exception as e:
            await self._session.rollback()
            raise exceptions.CargoCantCreateError(cargo_type) from e
        else:
            await self._session.refresh(instance)
            return instance
        finally:
            await self._session.close()


class RateRepository(BaseRepository[Rate]):

    def __init__(self) -> None:
        super().__init__(Rate, async_session())

    async def create_or_update(self, cargo_id: int, date: datetime.date, rate: float) -> Rate:
        instance = await self._session.scalar(
            select(Rate).where(self._model.cargo_id == cargo_id).where(self._model.date == date)
        )
        if instance:
            instance.rate = rate
            await self._session.commit()
            return instance
        try:
            instance = self._model.new_rate(cargo_id=cargo_id, date=date, rate=rate)
            self._session.add(instance)
            await self._session.commit()
        except Exception as e:
            await self._session.rollback()
            raise exceptions.RateCantCreateError(cargo_id=cargo_id, date=date, rate=rate) from e
        else:
            await self._session.refresh(instance)
            return instance
        finally:
            await self._session.close()


cargo_repository = CargoRepository()
rate_repository = RateRepository()
