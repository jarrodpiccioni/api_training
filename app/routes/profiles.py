import uuid
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.storage import load_profiles_data, save_profiles_data
from app.schemas import ProfileCreate, ProfileView, ProfileUpdate

router = APIRouter(prefix="/api/v1", tags=["profile"])

@router.get("/profile", response_model=ProfileView)
# View Profile
# Use a Dependency to fetch the authenticated user's profile
async def get_profile():
  profiles = load_profiles_data()
  if not profiles:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
  return profiles[0]

'''
@router.post("/profiles")
# Create Profile
# Use status_code=200 (Created) on success
async def create_profile():

@router.get("/profile-check/{phone_number}")
# Check Profile Status
# Use a separate endpoint to satisfy the requirement to "Check if the user has an account or not first - using Phone Number and Name"
'''