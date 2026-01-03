from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.trip import TripCreate, TripOut
from app.services.trip_service import create_trip, get_user_trips
from app.core.database import get_db
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/trips", tags=["Trips"])


@router.post("/", response_model=TripOut)
def create_trip_handler(
    data: TripCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_trip(db, current_user.id, data)


@router.get("/", response_model=list[TripOut])
def list_user_trips_handler(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_trips(db, current_user.id)
