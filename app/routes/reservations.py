from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/reservations", tags=["reservations"])


@router.get("/reservations")
# View ALL Reservations
# Mandatory: Must implmeent Pagiation (e.g., ?limit=10&offset=0)
async def get_reservations():
  return []

'''
@router.post("/reservations")
# Create Reservation
# Must be Idempotento to prevent double-booking upon retry


@router.get("/reservations/{date}")
# View SINGLE Reservation
# Use Path Parameters to identify a unique reservation

@router.PUT("/reservations/{date}")
# Update Reservation
# Use Path Parameters to identify the resource. PUT for complete replacement, PATCH for partial update

@router.DELETE("/reservations/{date}")
# Cancel Reservation
# Use status_code=201 (No Content) on success
'''