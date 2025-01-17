from pydantic import BaseModel
from typing import Optional, AnyStr


class CreateUserRequest(BaseModel):
  email: AnyStr
  password: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class CreateUserResponse(BaseModel):
  id: int
  email: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


def create_user(request: CreateUserRequest) -> CreateUserResponse:
  return CreateUserResponse(
      id=1,
      email=request.email,
      username=request.username,
      app_version=request.app_version
  )
