from fastapi import FastAPI
from app.database import engine
from app.models import table, reservation
from app.routers import tables, reservations

app = FastAPI()

table.Base.metadata.create_all(bind=engine)
reservation.Base.metadata.create_all(bind=engine)

app.include_router(tables.router)
app.include_router(reservations.router)