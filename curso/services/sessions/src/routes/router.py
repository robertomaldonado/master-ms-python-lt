from fastapi import APIRouter, Depends, Request

from src.providers.controllers.sessions import provide_sessions_controller
from src.routes.controllers.sessions import SessionsController
from src.routes.dtos.sessions import GenerateSessionRequest, SessionResponse, VerifyResponse

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/")
def generate_session(
    req: GenerateSessionRequest,
    controller: SessionsController = Depends(provide_sessions_controller),
) -> SessionResponse:
    return controller.generate(user_id=req.user_id)


@router.post("/verify")
def verify_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)) -> VerifyResponse:
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    return controller.verify(access_token)


@router.put("/refresh")
def refresh_session(req: Request, controller: SessionsController = Depends(provide_sessions_controller)) -> SessionResponse:
    access_token = req.headers.get("Authorization", "Bearer ").replace("Bearer ", "")
    refresh_token = req.headers.get("Refresh-Token", "")

    return controller.refresh(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.delete("/reject")
def reject_session():
    # TODO: Implementar
    return {"status": "ok"}


@router.delete("/reject/global")
def reject_global_session():
    # TODO: Implementar
    return {"status": "ok"}
