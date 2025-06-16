## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from fastapi import APIRouter, status
from schemas.event import EventCreate, Event
from services.event_service import *

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create(event: EventCreate):
    return create_event(event)

@router.get("/")
def list_events():
    return get_all_events()

@router.patch("/{event_id}/close", status_code=status.HTTP_200_OK)
def close(event_id: str):
    return close_event(event_id)

