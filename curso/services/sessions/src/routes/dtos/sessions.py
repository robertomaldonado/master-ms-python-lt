from datetime import datetime

from pydantic import BaseModel


class GenerateSessionRequest(BaseModel):
    user_id: int


class SessionResponse(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
    expires_at: datetime


class VerifyResponse(BaseModel):
    valid: bool
