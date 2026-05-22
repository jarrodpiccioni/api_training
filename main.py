from fastapi import FastAPI
from app.routes.profiles import router as profiles_router
from app.routes.reservations import router as reservations_router

"""
No AI used - all hand-coded.

Instructions: https://docs.google.com/document/d/16nB2sOOswO9x7Iiub7LiqOEXsaKfk0v-k4tlxxdaG94/edit?tab=t.0

Resources Used:
- https://devsheets.io/sheets/fastapi
- https://www.youtube.com/watch?v=8TMQcRcBnW8
"""
app = FastAPI()

app.include_router(profiles_router)
app.include_router(reservations_router)

@app.get("/health")
async def health_check():
  return {"status": "ok"}
