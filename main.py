from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.routes.profiles import router as profiles_router
from app.routes.reservations import router as reservations_router

from app.middleware.timer import timer_middleware

from app.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
"""
Instructions: https://docs.google.com/document/d/16nB2sOOswO9x7Iiub7LiqOEXsaKfk0v-k4tlxxdaG94/edit?tab=t.0

Resources Used:
- https://devsheets.io/sheets/fastapi
- https://www.youtube.com/watch?v=8TMQcRcBnW8
"""
app = FastAPI()

app.middleware("http")(timer_middleware)

app.include_router(profiles_router)
app.include_router(reservations_router)


@app.post("/token")
async def login(form: OAuth2PasswordRequestForm = Depends()):
  user = await authenticate_user(form.username, form.password)
  if not user:
    raise HTTPException(status_code=401, detail="Invalid credentials")
  token = create_access_token(
    data={"sub": user["username"]},
    expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
  )
  return {"access_token": token, "token_type": "bearer"}