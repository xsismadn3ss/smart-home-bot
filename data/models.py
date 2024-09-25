from dataclasses import dataclass
from datetime import datetime


@dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
class User:
    id: int
    chat_id: int


@dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
class Temperature:
    id: int
    value: int
    date: datetime

    @property
    def time(self):
        return f"{self.date.hour}:{self.date.minute}:{self.date.second}"


@dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
class Humidity:
    id: int
    value: int
    date: datetime
