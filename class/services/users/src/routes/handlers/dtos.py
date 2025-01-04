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