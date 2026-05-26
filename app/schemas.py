import re
from pydantic import BaseModel, Field, BeforeValidator
from enum import Enum
from typing import Optional, List, Annotated
from datetime import date, time

def clean_phone_number(value: str) -> str:
  cleaned = re.sub(r'\D', '', value)
  if len(cleaned) == 11 and cleaned[0] in ['0','1']:
    cleaned = cleaned[1:]
  if len(cleaned) != 10:
    raise ValueError("Phone number must contain exactly 10 digits")
  return cleaned

CleanPhoneNumber = Annotated[str, BeforeValidator(clean_phone_number)]

class ProfileCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: CleanPhoneNumber
  email: str
  postal_code: str
  age: int = Field(ge=21, description="Must be 21 or older")

class ProfileView(BaseModel):
  id: str
  name: str
  phone_number: CleanPhoneNumber
  email: str
  postal_code: str
  age: int
  created_by: str


class ProfileUpdate(BaseModel):
  name: Optional[str] = Field(min_length=3, max_length=30, default=None)
  phone_number: Optional[CleanPhoneNumber] = None
  email: Optional[str] = None
  postal_code: Optional[str] = None
  age: Optional[int] = Field(ge=21, description="Must be 21 or older", default=None)

class ReservationOccasion(str, Enum):
  bday = "Birthday"
  anniv = "Anniversary"
  other = "Other"

class ReservationCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: CleanPhoneNumber
  num_guests: int = Field(ge=1)
  occasion: Optional[ReservationOccasion] = None
  date: date
  time: time

class ReservationView(BaseModel):
  id: str
  name: str
  phone_number: CleanPhoneNumber
  num_guests: int
  occasion: Optional[ReservationOccasion] = None
  date: date
  time: time

class PaginatedReservationView(BaseModel):
  reservations: List[ReservationView]
  total: int

class ReservationCreatedConfirm(BaseModel):
  reservation: ReservationView
  message: str
  reservation_id: str

class ReservationUpdate(BaseModel):
  name: Optional[str] = Field(min_length=3, max_length=30, default=None)
  phone_number: Optional[CleanPhoneNumber] = None
  num_guests: Optional[int] = Field(ge=1, default=None)
  occasion: Optional[ReservationOccasion] = None
  date: Optional[date] = None
  time: Optional[time] = None
