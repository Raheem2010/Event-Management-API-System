## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from fastapi import APIRouter, HTTPException, status
from schemas.registration import Registration
from services.registration_service import *
from uuid import uuid4
from datetime import datetime

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Registration)
def register(user_id: str, event_id: str):
    return register_user(user_id, event_id)

@router.get("/", status_code=status.HTTP_200_OK)
def list_all():
    return get_all_registrations()

@router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user_regs(user_id: str):
    return get_registrations_by_user(user_id)

@router.patch("/{reg_id}/attend", status_code=status.HTTP_200_OK)
def mark_attended(reg_id: str):
    return mark_user_attendance(reg_id)
