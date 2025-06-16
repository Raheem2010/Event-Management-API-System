## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  

from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class Speaker(BaseModel):
    id: UUID
    name: str
    topic: str
    event_id: Optional[int] = None
    