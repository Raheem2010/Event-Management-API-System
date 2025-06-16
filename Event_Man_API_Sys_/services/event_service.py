## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from uuid import uuid4
from fastapi import HTTPException, status
from database import events
from schemas.event import Event, EventCreate

def create_event(data: EventCreate):
    event = Event(id=uuid4(), **data.dict())
    events.append(event)
    return event

def get_all_events():
    return events

def close_event(event_id: str):
    for e in events:
        if str(e.id) == event_id:
            e.is_open = False
            return {"detail": "Event closed successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {event_id} not found")

