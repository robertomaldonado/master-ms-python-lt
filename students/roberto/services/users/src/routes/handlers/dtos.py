from pydantic import BaseModel
from typing import Dict, List, Optional, AnyStr


class CreateUserRequest(BaseModel):
  email: AnyStr
  password: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class UserResponse(BaseModel):
  id: int
  email: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class PaginationMetadata(BaseModel):
  total: int
  page: int
  limit: int


class ListUsersResponse(BaseModel):
  data: List[UserResponse]
  meta: PaginationMetadata
