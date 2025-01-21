from fastapi import APIRouter, Depends

from src.routes.controllers.session import SessionsController
from src.providers.controllers.sessions import provide_sessions_controller
from src.routes.dtos.session import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/session/login")
def login(req: LoginRequest, controller: SessionsController = Depends(provide_sessions_controller)) -> LoginResponse:
    return controller.login(email=req.email, password=req.password)


@router.post("/session/logout")
def logout():
    return {"status": "ok"}
