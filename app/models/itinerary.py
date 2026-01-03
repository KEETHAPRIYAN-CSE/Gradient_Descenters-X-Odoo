from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)

    day = Column(Integer, nullable=False)
    title = Column(String(200))
    notes = Column(Text)

    created_at = Column(Date, server_default=func.now())

    trip = relationship("Trip", backref="itineraries")
