## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  

from pydantic import BaseModel
from uuid import UUID
from datetime import date

class EventBase(BaseModel):
    title: str
    location: str
    date: date

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: UUID
    is_open: bool = True
