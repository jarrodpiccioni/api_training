from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from app.routes.profiles import router as profiles_router
from app.routes.reservations import router as reservations_router
from app.storage import load_users_data

"""
Instructions: https://docs.google.com/document/d/16nB2sOOswO9x7Iiub7LiqOEXsaKfk0v-k4tlxxdaG94/edit?tab=t.0

Resources Used:
- https://devsheets.io/sheets/fastapi
- https://www.youtube.com/watch?v=8TMQcRcBnW8
"""
app = FastAPI()

app.include_router(profiles_router)
app.include_router(reservations_router)

SECRET_KEY = "My_secret_key_for_this_FastAPI_training_project_lets_go"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
  return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
  to_encode.update({"exp": expire})
  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithems=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
      raise HTTPException(status_code=401, detail="Invalid token")
  except JWTError:
    raise HTTPException(status_code=401, detail="Invalid token")
  user = get_user_from_db(username)
  if user is None:
    raise HTTPException(status_code=401, detail="User not found")
  return user

async def get_user_from_db(username: str):
  users = load_users_data()
  for user in users:
    if user["username"] == username:
      return user
  return None

async def authenticate_user(username: str, password: str):
  user = await get_user_from_db(username)

  # Debugging
  print(f"DATABASE FOUND USER: {user}")
  print(f"PASSWORD MATCHES: {verify_password(password, user['password']) if user else 'N/A'}")

  if not user or not verify_password(password, user["password"]):
    return False
  return user

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
