from fastapi import APIRouter, Depends
from .handlers.create_user import CreateUserRequest, CreateUserResponse, create_user
# <recurso>/{id}/<sub-recurso>/{sub-id}

router = APIRouter()


@router.get("/.health")
def health():
  return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest) -> CreateUserResponse:
  return create_user(request)


@router.put("/{id}")
def update_user_route(id: int):
  # Updated user
  return {
      "id": id,
      "message": "User updated"
  }


@router.get("/{id}")
def get_user_route(id: int):
  # User info
  return {
      "id": id
  }


@router.get("/")
def list_users_route() -> list:
  return [
      {"id": 456}
  ]
