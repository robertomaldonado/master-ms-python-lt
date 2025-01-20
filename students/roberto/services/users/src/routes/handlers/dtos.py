from pydantic import BaseModel
from typing import Dict, List, Optional, AnyStr

# Requests DTOs


class CreateUserRequest(BaseModel):
  email: AnyStr
  password: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class UpdateUserRequest(BaseModel):
  email: AnyStr
  password: AnyStr
  username: AnyStr
  app_version: Optional[AnyStr] = None


class GetUserRequest(BaseModel):
  id: int


class DeleteUserRequest(BaseModel):
  id: int

# Response DTOs


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


class DeleteUserResponse(BaseModel):
  id: int
  isDeleted: bool
