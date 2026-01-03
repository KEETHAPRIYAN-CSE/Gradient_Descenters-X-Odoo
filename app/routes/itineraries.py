from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.itinerary import ItineraryCreate, ItineraryOut
from app.services.itinerary_service import create_itinerary, get_trip_itineraries
from app.core.database import get_db
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/itineraries", tags=["Itineraries"])


@router.post("/{trip_id}", response_model=ItineraryOut)
def add_itinerary(trip_id: int, data: ItineraryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_itinerary(db, trip_id, data)


@router.get("/{trip_id}", response_model=list[ItineraryOut])
def list_itineraries(trip_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_trip_itineraries(db, trip_id)
