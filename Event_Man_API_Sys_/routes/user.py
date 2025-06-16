## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428  
from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate, User
from services.user_service import *

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate):
    return create_user(user)

@router.get("/", status_code=status.HTTP_200_OK)
def list_users():
    return get_all_users()

@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update(user_id: str, user: UserCreate):
    return update_user(user_id, user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)	
def delete(user_id: str):
    return delete_user(user_id)

@router.patch("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
def deactivate(user_id: str, ):
    return deactivate_user(user_id)
