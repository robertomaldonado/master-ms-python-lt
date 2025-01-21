from fastapi import APIRouter

from .handlers.dtos import CreateUserRequest, UserResponse, ListUserResponse, UpdateUserRequest, UpdateUserResponse, GetUserRequest, GetUserResponse, DeleteUserRequest, DeleteUserResponse
from .handlers.create_user import create_user
from .handlers.list_all_users import list_users
from .handlers.update_user import update_user
from .handlers.get_user import get_user
from .handlers.delete_user import delete_user

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}

@router.post("/")
def create_user_route(request: CreateUserRequest) -> UserResponse:
    return create_user(request)

@router.put("/{user_id}")
def update_user_route(request: UpdateUserRequest) -> UpdateUserResponse:
    return update_user(request)

@router.get("/user/{user_id}", response_model=GetUserResponse)
def get_user_route(user_id: int):
    request = GetUserRequest(id=user_id)
    return get_user(request)

@router.get("/")
def list_user_route() -> ListUserResponse:
    return list_users()

@router.delete("/user/{user_id}", response_model=DeleteUserResponse)
def delete_user_route(user_id: int):
    request = DeleteUserRequest(id=user_id)
    return delete_user(request)