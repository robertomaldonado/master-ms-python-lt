from typing import Optional, AnyStr, List
from pydantic import BaseModel


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

class ListUserResponse(BaseModel):
    data: List[UserResponse]
    meta: PaginationMetadata


class UpdateUserRequest(BaseModel):
    id: int
    email: Optional[AnyStr] = None
    username: Optional[AnyStr] = None
    app_version: Optional[AnyStr] = None

class UpdateUserResponse(UserResponse):
    data: List[UserResponse]

class GetUserRequest(BaseModel):
    id: int

class GetUserResponse(UserResponse):
    extra_info: Optional[str] = None

class DeleteUserRequest(BaseModel):
    id: int

class DeleteUserResponse(BaseModel):
    success: bool
    message: Optional[str] = "Usuario eliminado"