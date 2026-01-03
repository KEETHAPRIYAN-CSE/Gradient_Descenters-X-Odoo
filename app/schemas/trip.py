from pydantic import BaseModel
from datetime import datetime

class TripCreate(BaseModel):
    title: str
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None

class TripOut(TripCreate):
    id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel
from datetime import date

class TripCreate(BaseModel):
    title: str
    destination: str
    start_date: date
    end_date: date

class TripOut(TripCreate):
    id: int

    class Config:
        from_attributes = True
