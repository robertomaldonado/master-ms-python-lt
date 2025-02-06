from fastapi import APIRouter, Depends, Request

from src.routes.controllers.session import SessionsController
from src.providers.controllers.sessions import provide_sessions_controller
from src.routes.dtos.session import LoginRequest, LoginResponse
from src.infra.environment import envs
from src.infra.http import path
from src.infra.logger import log


router = APIRouter()
prefix = envs.get("PATH_PREFIX", "")


@router.post(path("/sessions/login", prefix))
def login(req: LoginRequest, controller: SessionsController = Depends(provide_sessions_controller)) -> LoginResponse:
    log.info("Login request", email=req.email)
    return controller.login(email=req.email, password=req.password)


@router.post(path("/sessions/logout", prefix))
def logout(req: Request, controller: SessionsController = Depends(provide_sessions_controller)):
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    refresh_token = req.headers.get("Refresh-Token", "")

    return controller.logout(access_token=access_token, refresh_token=refresh_token)
