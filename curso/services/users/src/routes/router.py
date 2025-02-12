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
from src.infra.environment import envs
from src.infra.http import path


router = APIRouter()
prefix = envs.get("PATH_PREFIX", "")


@router.post(path("/", prefix))
def create_user_route(request: CreateUserRequest, controller: UsersController = Depends(provide_users_controller)) -> UserResponse:
    return controller.create(request)


@router.get(path("/", prefix))
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


@router.get(path("all", prefix))
def list_all_users_route(controller: UsersController = Depends(provide_users_controller)) -> ListAllUsersResponse:
    return controller.list_all()


@router.put(path("/{user_id}", prefix))
def update_user_route(
        req: UpdateUserRequest,
        user_id: int,

        controller: UsersController = Depends(provide_users_controller)
)-> UserResponse:
    return controller.update(user_id, req)


@router.get(path("/{user_id}", prefix))
def get_user_route(user_id: int, controller: UsersController = Depends(provide_users_controller)) -> UserResponse:
    return controller.get(user_id)


@router.delete(path("/{user_id}", prefix))
def delete_user_route(user_id: int, controller: UsersController = Depends(provide_users_controller)) -> DeleteUserResponse:
    return controller.delete(user_id)
