from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

"""
Profile Creation
- Full Name
- Phone Number
- Email
- Postal Code
- Age (always greater than 21 years old)

Create Reservation
- Name
- Phone Number
- Number of guests
- Occasion (optional)
- Date
- Time
"""
class ProfileCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: str
  email: str
  postal_code: str
  age: int = Field(ge=21, description="Must be 21 or older")

# class ProfileUpdate(BaseModel):


class ReservationOccasion(str, Enum):
  bday = "Birthday"
  anniv = "Anniversary"
  other = "Other"

class ReservationCreate(BaseModel):
  name: str = Field(min_length=3, max_length=30)
  phone_number: str
  num_guests: int = Field(ge=1)
  occasion: ReservationOccasion

# class ReservationUpdate(BaseModel):

