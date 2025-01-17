from fastapi import APIRouter, Depends
from .handlers.create_user import CreateUserRequest, CreateUserResponse, create_user
from .handlers.update_user import UpdateUserRequest, UpdateUserResponse, update_user
from .handlers.delete_user import DeleteUserResponse, delete_user
from .handlers.get_user import GetUserResponse, get_user

router = APIRouter()


@router.get("/.health")
def health():
  return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest) -> CreateUserResponse:
  return create_user(request)


@router.put("/{id}")
def update_user_route(request: UpdateUserRequest) -> UpdateUserResponse:
  return update_user(request)


@router.get("/{id}")
def get_user_route(id: int) -> GetUserResponse:
  return get_user(id)


@router.get("/")
def list_users_route() -> list:
  return [
      {"id": 456}
  ]


@router.delete("/{id}")
def delete_user_route(id: int) -> DeleteUserResponse:
  return delete_user(id)
