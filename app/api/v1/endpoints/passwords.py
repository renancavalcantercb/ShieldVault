from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.password_service import create_password, list_passwords
from app.schemas.password import PasswordCreate, PasswordResponse
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
