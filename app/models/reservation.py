from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    table_id = Column(Integer, ForeignKey("tables.id"), index=True)
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)