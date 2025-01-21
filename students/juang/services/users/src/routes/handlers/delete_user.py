from .dtos import DeleteUserRequest, DeleteUserResponse
from fastapi import HTTPException

FAKEDATABASE = {
    1: {"id": 1, "email": "user1@example.com", "username": "user1"},
    2: {"id": 2, "email": "user2@example.com", "username": "user2"},
}


def delete_user(request: DeleteUserRequest) -> DeleteUserResponse:

    if request.id not in FAKEDATABASE:
        raise HTTPException(status_code=404, detail=f"Usuario con ID {request.id} no encontrado")

    del FAKEDATABASE[request.id]
    return DeleteUserResponse(success=True, message="Usuario eliminado")