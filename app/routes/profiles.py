from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["profile"])


@router.get("/profile")
# View Profile
# Use a Dependency to fetch teh authenticated user's profile
async def get_profile():
  return []

'''
@router.post("/profiles")
# Create Profile
# Use status_code=200 (Created) on success
async def create_profile():

@router.get("/profile-check/{phone_number}")
# Check Profile Status
# Use a separate endpoint to satisfy the requirement to "Check if the user has an account or not first - using Phone Number and Name"
'''