from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class PasswordCreate(BaseModel):
    service_name: str = Field(..., example="Google")
    username: str = Field(..., example="user@gmail.com")
    password: str = Field(..., example="strongpassword123")
    notes: Optional[str] = Field(None, example="Minha conta principal do Google")
    url: Optional[HttpUrl] = Field(None, example="https://google.com")

class PasswordResponse(BaseModel):
    id: int
    service_name: str
    username: str
    notes: Optional[str]
    url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class PasswordUpdate(BaseModel):
    service_name: Optional[str] = Field(None, example="Google")
    username: Optional[str] = Field(None, example="user@gmail.com")
    password: Optional[str] = Field(None, example="newstrongpassword123")
    notes: Optional[str] = Field(None, example="Conta atualizada")
    url: Optional[HttpUrl] = Field(None, example="https://new-url.com")
