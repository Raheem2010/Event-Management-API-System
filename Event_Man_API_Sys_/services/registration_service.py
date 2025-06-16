## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from uuid import uuid4
from database import users, events, registrations
from schemas.registration import Registration
from datetime import datetime
from fastapi import HTTPException, status

def register_user(user_id: str, event_id: str):
    user = next((u for u in users if str(u.id) == user_id and u.is_active), None)
    event = next((e for e in events if str(e.id) == event_id and e.is_open), None)
    

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id}  not found or inactive"
        )

    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id {event_id} not found or closed")
    
    if any(r for r in registrations if str(r.user_id) == user_id and str(r.event_id) == event_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already registered for this event"
        )
        
    reg = Registration(
        id=uuid4(), user_id=user.id, event_id=event.id,
        registration_date=datetime.now()
    )
    registrations.append(reg)
    return reg

def get_all_registrations():
    return registrations

def get_registrations_by_user(user_id: str):
    user_regs = [r for r in registrations if str(r.user_id) == user_id]
    if not user_regs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registrations found for this user")
    return user_regs

def mark_user_attendance(reg_id: str):
    for r in registrations:
        if str(r.id) == reg_id:
            r.attended = True
            return r
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Registration with id {reg_id} not found")
