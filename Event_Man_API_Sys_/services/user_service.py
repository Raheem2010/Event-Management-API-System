## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from uuid import uuid4, UUID
from fastapi import HTTPException, status, Response
from database import users
from schemas.user import User, UserCreate

def create_user(user_data: UserCreate):
    if any(u.email == user_data.email for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
    user = User(id=uuid4(), **user_data.dict())
    users.append(user)
    return user

def get_all_users():
    return users

def update_user(user_id: str, new_data: UserCreate,):
    for u in users:
        if str(u.id) == user_id:
            u.name = new_data.name
            u.email = new_data.email
            return {"data": u}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} does not exist")

def delete_user(user_id: str):
    global users
    for index, user in enumerate(users):
        if str(user.id) == user_id:
            users.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} does not exist")

def deactivate_user(user_id: str):
    for u in users:
        if str(u.id) == user_id:
            u.is_active = False
            return u
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")