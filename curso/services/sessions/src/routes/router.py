from fastapi import APIRouter, Depends, Request

from src.providers.controllers.sessions import provide_sessions_controller
from src.routes.controllers.sessions import SessionsController
from src.routes.dtos.sessions import GenerateSessionRequest, SessionResponse, VerifyResponse
from src.infra.environment import envs
from src.infra.http import path

router = APIRouter()

prefix = envs.get("PATH_PREFIX", "")


@router.get(path(".health", prefix))
def health():
    return {"status": "ok"}


@router.post(path("/", prefix))
def generate_session(
    req: GenerateSessionRequest,
    controller: SessionsController = Depends(provide_sessions_controller),
) -> SessionResponse:
    return controller.generate(user_id=req.user_id)


@router.post(path("verify", prefix))
def verify_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)) -> VerifyResponse:
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    return controller.verify(access_token)


@router.put(path("refresh", prefix))
def refresh_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)) -> SessionResponse:
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    refresh_token = req.headers.get("Refresh-Token", "")

    return controller.refresh(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.delete(path("reject", prefix))
def reject_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)):
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    refresh_token = req.headers.get("Refresh-Token", "")

    controller.reject(
        access_token=access_token,
        refresh_token=refresh_token
    )

    return {"status": "ok"}


@router.delete(path("reject/global", prefix))
def reject_global_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)):
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    refresh_token = req.headers.get("Refresh-Token", "")

    controller.reject_global(
        access_token=access_token,
        refresh_token=refresh_token
    )

    return {"status": "ok"}
