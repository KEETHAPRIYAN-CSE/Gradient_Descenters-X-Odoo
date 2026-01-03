from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)

    owner_id = Column(Integer, ForeignKey("users.id"))

