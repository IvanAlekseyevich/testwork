import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(default=func.now(), nullable=False, onupdate=func.now())


class Rate(Base):
    __tablename__ = "rate"
    cargo_id: Mapped[int] = mapped_column(ForeignKey("cargo.id"))
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    rate: Mapped[float] = mapped_column(default=0, nullable=False)
    cargo: Mapped["Cargo"] = relationship(back_populates="rate", lazy="selectin")

    @classmethod
    def new_rate(cls, cargo_id: int, date: datetime.date, rate: float) -> "Rate":
        return cls(
            cargo_id=cargo_id,
            date=date,
            rate=rate,
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}("
            f"id={self.id!r}, "
            f"cargo_id={self.cargo_id!r}, "
            f"start_date={self.date!r}, "
            f"rate={self.rate!r})"
        )


class Cargo(Base):
    __tablename__ = "cargo"
    cargo_type: Mapped[str] = mapped_column(unique=True)
    rate: Mapped[list["Rate"]] = relationship(back_populates="cargo")

    @classmethod
    def new_cargo(cls, cargo_type: str) -> "Cargo":
        return cls(cargo_type=cargo_type)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}("
            f"id={self.id!r}, "
            f"cargo_type={self.cargo_type!r})"
        )
