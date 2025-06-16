## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from fastapi import APIRouter, HTTPException, status
from database import speakers

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/", status_code=status.HTTP_200_OK)
def list_speakers():
    return speakers
