from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.password_service import create_password, list_passwords, edit_password
from app.schemas.password import PasswordCreate, PasswordResponse, PasswordUpdate
from app.core.security import get_current_user, get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=PasswordResponse, status_code=status.HTTP_201_CREATED)
def create_password_endpoint(
    password_data: PasswordCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user.id
    return create_password(db, user_id, password_data)


@router.get("/", response_model=List[PasswordResponse], status_code=status.HTTP_200_OK)
def list_passwords_endpoint(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user.id
    return list_passwords(db, user_id)


@router.put("/{password_id}", response_model=PasswordResponse, status_code=status.HTTP_200_OK)
def update_password_endpoint(
    password_id: int,
    password_data: PasswordUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user.id
    updated_password = edit_password(db, user_id, password_id, password_data)
    if not updated_password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password not found or unauthorized")
    return updated_password
