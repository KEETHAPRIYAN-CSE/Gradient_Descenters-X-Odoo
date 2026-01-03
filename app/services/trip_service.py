from sqlalchemy.orm import Session
from app.models.trip import Trip

def create_trip(db: Session, user_id: int, data):
    trip = Trip(
        title=data.title,
        description=data.description,
        start_date=data.start_date,
        end_date=data.end_date,
        owner_id=user_id
    )
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

def get_user_trips(db: Session, user_id: int):
    return db.query(Trip).filter(Trip.owner_id == user_id).all()

from sqlalchemy.orm import Session
from app.models.trip import Trip

def create_trip(db: Session, trip_data, user_id: int):
    trip = Trip(**trip_data.dict(), owner_id=user_id)
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

def get_user_trips(db: Session, user_id: int):
    return db.query(Trip).filter(Trip.owner_id == user_id).all()
