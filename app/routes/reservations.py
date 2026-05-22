import uuid
from fastapi import APIRouter, HTTPException, status
from app.storage import load_reservations_data, save_reservations_data
from app.schemas import ReservationUpdate, ReservationView, ReservationOccasion

router = APIRouter(prefix="/api/v1/reservations", tags=["reservations"])


@router.get("/", response_model=list[ReservationView])
# View ALL Reservations
# Mandatory: Must implmeent Pagiation (e.g., ?limit=10&offset=0)
async def get_reservations():
  reservations = load_reservations_data()
  return reservations

'''
@router.post("/")
# Create Reservation
# Must be Idempotento to prevent double-booking upon retry

@router.get("/{date}")
# View SINGLE Reservation
# Use Path Parameters to identify a unique reservation

@router.PUT("/{date}")
# Update Reservation
# Use Path Parameters to identify the resource. PUT for complete replacement, PATCH for partial update

@router.DELETE("/{date}")
# Cancel Reservation
# Use status_code=201 (No Content) on success
'''