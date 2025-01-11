from typing import Optional

from fastapi import APIRouter, Depends

from .handlers.dtos import (
    CreateUserRequest,
    UserResponse,
    ListAllUsersResponse,
    DeleteUserResponse,
    UpdateUserRequest,
    SearchUsersResponse
)
from .handlers.create_user import create_user
from .handlers.list_all_users import list_all_users
from .handlers.search_users import search_users
from .handlers.update_user import update_user
from .handlers.delete_user import delete_user
from .handlers.get_user import get_user
from ..domain.services import UserService

from src.providers.domain.services.user import provide_user_service

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest, user_service: UserService = Depends(provide_user_service)) -> UserResponse:
    return create_user(request, user_service)


@router.get("/")
def search_users_route(
        # Query parameters
        email: Optional[str] = None,
        username: Optional[str] = None,
        app_version: Optional[str] = None,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,

        # Dependency injection
        user_service: UserService = Depends(provide_user_service),
) -> SearchUsersResponse:
    return search_users(
        user_service,
        email=email,
        username=username,
        app_version=app_version,
        page=page,
        limit=limit
    )


@router.get("/all")
def list_all_users_route(user_service: UserService = Depends(provide_user_service)) -> ListAllUsersResponse:
    return list_all_users(user_service)


@router.put("/{user_id}")
def update_user_route(req: UpdateUserRequest, user_id: int, user_service: UserService = Depends(provide_user_service))-> UserResponse:
    return update_user(user_id, req, user_service)


@router.get("/{user_id}")
def get_user_route(user_id: int, user_service: UserService = Depends(provide_user_service)) -> UserResponse:
    return get_user(user_id, user_service)


@router.delete("/{user_id}")
def delete_user_route(user_id: int, user_service: UserService = Depends(provide_user_service)) -> DeleteUserResponse:
    return delete_user(user_id, user_service)
