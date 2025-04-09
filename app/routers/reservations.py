from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reservation import Reservation
from app.models.table import Table
from app.schemas.reservation import ReservationCreate, Reservation as ReservationSchema
from app.services.reservation_service import check_reservation_conflict

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[ReservationSchema])
def get_reservations(db: Session = Depends(get_db)):
    reservations = db.query(Reservation).all()
    return reservations

@router.post("/", response_model=ReservationSchema)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == reservation.table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail=f"Table with id {reservation.table_id} not found")
    if check_reservation_conflict(db, reservation.table_id, reservation.reservation_time, reservation.duration_minutes):
        raise HTTPException(status_code=400, detail="Table is already reserved for this time slot")
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail=f"Reservation with id {reservation_id} not found")
    db.delete(reservation)
    db.commit()
    return {"message": "Reservation deleted"}