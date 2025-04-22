from datetime import datetime, timedelta
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, verify_password
from schemas.token import TokenData
from schemas.user import UserCreate, User
from services.user import user_service


user_router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

@user_router.post("/register")
def create_user(user_data: UserCreate):
    user = user_service.create_user(user_data)
    return {"message": "user created successfully", "data": user}


@user_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: User = user_service.get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode = TokenData(id=user.id, email=user.email).model_dump()
    access_token = create_access_token(
        data=data_to_encode, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/users/{user_id}", response_model=User)
def get_user_details(user_id: str):
    return user_service.get_user_by_id(user_id)
