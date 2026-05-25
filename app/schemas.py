from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List

class ProfileCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: str
  email: str
  postal_code: str
  age: int = Field(ge=21, description="Must be 21 or older")

class ProfileView(BaseModel):
  id: str
  name: str
  phone_number: str
  email: str
  postal_code: str
  age: int
  created_by: str


class ProfileUpdate(BaseModel):
  name: Optional[str] = Field(min_length=3, max_length=30)
  phone_number: Optional[str]
  email: Optional[str]
  postal_code: Optional[str]
  age: Optional[int] = Field(ge=21, description="Must be 21 or older")

class ReservationOccasion(str, Enum):
  bday = "Birthday"
  anniv = "Anniversary"
  other = "Other"

class ReservationCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: str
  num_guests: int = Field(ge=1)
  occasion: Optional[ReservationOccasion] = None
  date: str
  time: str

class ReservationView(BaseModel):
  id: str
  name: str
  phone_number: str
  num_guests: int
  occasion: Optional[ReservationOccasion] = None
  date: str
  time: str

class PaginatedReservationView(BaseModel):
  reservations: List[ReservationView]
  total: int

class ReservationCreatedConfirm(BaseModel):
  reservation: ReservationView
  message: str
  reservation_id: str

class ReservationUpdate(BaseModel):
  name: Optional[str] = Field(min_length=3, max_length=30)
  phone_number: Optional[str]
  num_guests: Optional[int] = Field(ge=1)
  occasion: Optional[ReservationOccasion]
  date: Optional[str]
  time: Optional[str]
