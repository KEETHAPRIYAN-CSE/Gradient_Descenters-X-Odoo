from sqlalchemy.orm import Session
from app.models.itinerary import Itinerary

def create_itinerary(db: Session, trip_id: int, data):
    itinerary = Itinerary(
        trip_id=trip_id,
        day=data.day,
        title=data.title,
        notes=data.notes
    )
    db.add(itinerary)
    db.commit()
    db.refresh(itinerary)
    return itinerary

def get_trip_itineraries(db: Session, trip_id: int):
    return db.query(Itinerary).filter(Itinerary.trip_id == trip_id).all()
