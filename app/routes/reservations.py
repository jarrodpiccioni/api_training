import uuid
from fastapi import APIRouter, HTTPException, status, Header, Depends
from app.auth import get_current_user
from app.storage import load_reservations_data, save_reservations_data
from app.schemas import ReservationUpdate, PaginatedReservationView, ReservationView, ReservationCreate, ReservationCreatedConfirm
from datetime import date

router = APIRouter(prefix="/api/v1/reservations", tags=["reservations"])

reservations = load_reservations_data()

# View ALL Reservations
# Mandatory: Must implmeent Pagiation (e.g., ?limit=10&offset=0)
@router.get("/", response_model=PaginatedReservationView)
async def get_reservations(skip: int = 0, limit: int = 10):
  if not reservations:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservations not found")
  return {"reservations": reservations[skip : skip + limit], "total": len(reservations)}

# Create Reservation
# Must be Idempotent to prevent double-booking upon retry
@router.post("/", response_model=ReservationCreatedConfirm)
async def create_reservation(reservation: ReservationCreate, current_user: dict = Depends(get_current_user), idempotency_key: str = Header()):
  new_reservation = {"id": uuid.uuid4().hex, **reservation.model_dump(), "created_by": current_user["username"], "idempotency_key": idempotency_key}
  for r in reservations:
    if r.get("idempotency_key") == idempotency_key:
      return {"reservation": r, "message": f"Reservation created successfully for {reservation.name} on {reservation.date} at {reservation.time} by {current_user['username']}", "reservation_id": r["id"], "idempotency_key": idempotency_key}
  reservations.append(new_reservation)
  save_reservations_data(reservations)
  return {"reservation": new_reservation, "message": f"Reservation created successfully for {reservation.name} on {reservation.date} at {reservation.time} by {current_user['username']}", "reservation_id": new_reservation["id"], "idempotency_key": idempotency_key}

# View SINGLE Reservation
# Use Path Parameters to identify a unique reservation
@router.get("/{date}")
async def get_reservation(date: date):
  for reservation in reservations:
    if reservation["date"] == date.isoformat():
      return reservation
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reservation not found for date: {date}")


# Cancel Reservation
# Use status_code=204 (No Content) on success
@router.delete("/{date}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_reservation(date: date):
  for reservation in reservations:
    if reservation["date"] == date.isoformat():
      reservations.remove(reservation)
      save_reservations_data(reservations)
      return None
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reservation not found for date: {date}")

# Update Reservation
# Use Path Parameters to identify the resource. PUT for complete replacement, PATCH for partial update
@router.patch("/{date}", response_model=ReservationView)
async def update_reservation(date: date, reservation_update: ReservationUpdate):
  for reservation in reservations:
    if reservation["date"] == date.isoformat():
      update_data = reservation_update.model_dump(exclude_unset=True, mode='json')
      reservation.update(update_data)
      save_reservations_data(reservations)
      return reservation
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Reservation not found for date: {date}")
