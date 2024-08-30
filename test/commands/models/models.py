from dataclasses import dataclass
from typing import Optional
import datetime


@dataclass(repr=True, order=True, eq=True, init=True)
class Spent:
    id: Optional[float | None]
    datatime: datetime.datetime
    value: str


@dataclass(repr=True, order=True, eq=True, init=True)
class Earn:
    id: Optional[int | None]
    datetime: datetime.datetime
    value:str

@dataclass()
class Graphics:
    id: Optional[int|None]
    datetime: datetime.datetime
    image: bytes