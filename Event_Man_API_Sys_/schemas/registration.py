## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Registration(BaseModel):
    id: UUID
    user_id: UUID
    event_id: UUID
    registration_date: datetime
    attended: bool = False