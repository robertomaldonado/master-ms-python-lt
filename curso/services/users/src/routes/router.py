from typing import Optional

from fastapi import APIRouter, Depends

from src.routes.controllers.users import UsersController
from src.routes.dtos.users import (
    CreateUserRequest,
    UserResponse,
    ListAllUsersResponse,
    DeleteUserResponse,
    UpdateUserRequest,
    SearchUsersResponse
)

from src.providers.controllers.users import provide_users_controller

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest, controller: UsersController = Depends(provide_users_controller)) -> UserResponse:
    return controller.create(request)


@router.get("/")
def search_users_route(
        # Query parameters
        email: Optional[str] = None,
        username: Optional[str] = None,
        app_version: Optional[str] = None,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,

        # Dependency injection
        controller: UsersController = Depends(provide_users_controller),
) -> SearchUsersResponse:
    return controller.search(
        email=email,
        username=username,
        app_version=app_version,
        page=page,
        limit=limit
    )


@router.get("/all")
def list_all_users_route(controller: UsersController = Depends(provide_users_controller)) -> ListAllUsersResponse:
    return controller.list_all()


@router.put("/{user_id}")
def update_user_route(
        req: UpdateUserRequest,
        user_id: int,

        controller: UsersController = Depends(provide_users_controller)
)-> UserResponse:
    return controller.update(user_id, req)


@router.get("/{user_id}")
def get_user_route(user_id: int, controller: UsersController = Depends(provide_users_controller)) -> UserResponse:
    return controller.get(user_id)


@router.delete("/{user_id}")
def delete_user_route(user_id: int, controller: UsersController = Depends(provide_users_controller)) -> DeleteUserResponse:
    return controller.delete(user_id)
