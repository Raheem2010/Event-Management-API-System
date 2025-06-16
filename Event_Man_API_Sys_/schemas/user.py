## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID
    is_active: bool = True
