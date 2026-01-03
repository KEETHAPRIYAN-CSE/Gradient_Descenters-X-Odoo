from pydantic import BaseModel

class ItineraryCreate(BaseModel):
    day: int
    title: str | None = None
    notes: str | None = None

class ItineraryOut(ItineraryCreate):
    id: int

    class Config:
        from_attributes = True
