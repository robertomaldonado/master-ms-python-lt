from pydantic import BaseModel
from typing import Optional, AnyStr


class GetUserRequest(BaseModel):
  id: int


class GetUserResponse(BaseModel):
  id: int
  email: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


def get_user(request: GetUserRequest) -> GetUserResponse:
  userExists = True  # Check if user exists based on id
  if userExists:
    return GetUserResponse(id=request,
                           email="Asociated mail",
                           username="Asociated username",
                           app_version="v0.0"
                           )
  else:
    return GetUserResponse(
        id=0,
        email="",
        username=""
    )
