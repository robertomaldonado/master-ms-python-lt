from fastapi import APIRouter

from .handlers.dtos import (
    CreateUserRequest,
    UserResponse,
    ListUserResponse,
    DeleteUserResponse,
    UpdateUserRequest
)
from .handlers.create_user import create_user
from .handlers.list_users import list_users
from .handlers.update_user import update_user
from .handlers.delete_user import delete_user
from .handlers.get_user import get_user


router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest) -> UserResponse:
    return create_user(request)


@router.put("/{user_id}")
def update_user_route(req: UpdateUserRequest, user_id: int)-> UserResponse:
    return update_user(user_id, req)


@router.get("/{user_id}")
def get_user_route(user_id: int) -> UserResponse:
    return get_user(user_id)


@router.get("/")
def list_users_route() -> ListUserResponse:
    return list_users()


@router.delete("/{user_id}")
def delete_user_route(user_id: int) -> DeleteUserResponse:
    return delete_user(user_id)
