from datetime import datetime

from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
    expires_at: datetime


class LogoutResponse(BaseModel):
    message: str
