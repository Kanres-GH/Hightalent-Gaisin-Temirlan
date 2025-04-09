from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from datetime import datetime, timedelta
from sqlalchemy.sql import func

def check_reservation_conflict(db: Session, table_id: int, start_time: datetime, duration: int):
    end_time = start_time + timedelta(minutes=duration)
    conflicting = db.query(Reservation).filter(
        Reservation.table_id == table_id,
        Reservation.reservation_time < end_time,
        (Reservation.reservation_time + func.make_interval(0, 0, 0, 0, 0, Reservation.duration_minutes)) > start_time
    ).first()
    return conflicting is not None