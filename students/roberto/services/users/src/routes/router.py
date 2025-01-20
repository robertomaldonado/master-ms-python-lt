from fastapi import APIRouter, Depends
from .handlers.create_user import create_user
from .handlers.update_user import UpdateUserRequest, update_user
from .handlers.delete_user import DeleteUserResponse, delete_user
from .handlers.get_user import get_user
from .handlers.list_users import ListUsersResponse, list_users
from .handlers.dtos import CreateUserRequest, UserResponse

router = APIRouter()


@router.get("/.health")
def health():
  return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest) -> UserResponse:
  return create_user(request)


@router.put("/{id}")
def update_user_route(request: UpdateUserRequest) -> UserResponse:
  return update_user(request)


@router.get("/{id}")
def get_user_route(id: int) -> UserResponse:
  return get_user(id)


@router.get("/")
def list_users_route() -> ListUsersResponse:
  return list_users()


@router.delete("/{id}")
def delete_user_route(id: int) -> DeleteUserResponse:
  return delete_user(id)
