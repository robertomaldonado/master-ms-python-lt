from fastapi import HTTPException

from .dtos import GetUserRequest,GetUserResponse

from src.domain.services.user import UserService

FAKEDATABASE = {
    1: {"id": 1, "email": "user1@example.com", "username": "user1", "password": "password1", "app_version": "1.0.0"},
    2: {"id": 2, "email": "user2@example.com", "username": "user2", "password": "password2", "app_version": "1.0.1"},
}

def get_user(request: GetUserRequest) -> GetUserResponse:
    user = FAKEDATABASE.get(request.id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return GetUserResponse(**user)