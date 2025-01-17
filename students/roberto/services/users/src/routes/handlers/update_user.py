from pydantic import BaseModel
from typing import Optional, AnyStr


class UpdateUserRequest(BaseModel):
  email: AnyStr
  password: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class UpdateUserResponse(BaseModel):
  id: int
  email: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


def update_user(request: UpdateUserRequest) -> UpdateUserResponse:
  return UpdateUserResponse(
      id=1,
      email=request.email,
      username=request.username,
      app_version=request.app_version
  )
