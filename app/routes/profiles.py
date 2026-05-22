import uuid
from fastapi import APIRouter, HTTPException, status, Depends
from app.storage import load_profiles_data, save_profiles_data
from app.schemas import ProfileCreate, ProfileView, ProfileUpdate
from app.auth import get_current_user

router = APIRouter(prefix="/api/v1", tags=["profile"])

# View Profile
# Use a Dependency to fetch the authenticated user's profile
@router.get("/profile", response_model=ProfileView)
async def get_profile(current_user: dict = Depends(get_current_user)):
  profiles = load_profiles_data()
  if not profiles:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
  for profile in profiles:
    if profile["created_by"] == current_user["username"]:
      return profile

'''

# Create Profile
# Use status_code=200 (Created) on success
@router.post("/profiles")
async def create_profile():
  profiles = load_profiles_data()
  if not profiles:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profiles not found")
  else
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Profiles loaded")
  return profiles

@router.get("/profile-check/{phone_number}")
# Check Profile Status
# Use a separate endpoint to satisfy the requirement to "Check if the user has an account or not first - using Phone Number and Name"
'''