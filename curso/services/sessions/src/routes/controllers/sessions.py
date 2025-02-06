from fastapi import HTTPException

from src.domain.services.sessions import SessionService
from src.routes.dtos.sessions import SessionResponse, VerifyResponse
from src.infra.logger import log


class SessionsController:
    def __init__(self, srv_sessions: SessionService):
        self.srv_sessions = srv_sessions

    def generate(self, user_id: int) -> SessionResponse:
        sess = self.srv_sessions.generate(user_id)

        return SessionResponse(
            user_id=sess.user_id,
            access_token=sess.access_token,
            refresh_token=sess.refresh_token,
            expires_at=sess.expires_at
        )

    def verify(self, access_token: str) -> VerifyResponse:
        if access_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        try:
            if not self.srv_sessions.verify(access_token):
                raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            log.error("Unexpected error", error=str(e))
            raise HTTPException(status_code=500, detail="Unexpected error")

        return VerifyResponse(
            valid=True
        )

    def refresh(self, access_token: str, refresh_token: str) -> SessionResponse:
        if access_token == "" or refresh_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        try:
            return self.srv_sessions.refresh(
                access_token=access_token,
                refresh_token=refresh_token
            )
        except ValueError as e:
            log.error("Unexpected error", error=str(e))
            raise HTTPException(status_code=401, detail="Invalid Tokens")

    def reject(self, access_token: str, refresh_token: str):
        if access_token == "" or refresh_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        try:
            self.srv_sessions.reject(
                access_token=access_token,
                refresh_token=refresh_token
            )
        except Exception as e:
            log.error("Unexpected error", error=str(e))
            raise HTTPException(status_code=500, detail="Unexpected error")

        return { "message": "session rejected" }

    def reject_global(self, access_token: str, refresh_token: str) -> bool:
        if access_token == "" or refresh_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        user_id = self.srv_sessions.get_user_id(access_token, refresh_token)

        return self.srv_sessions.global_reject(user_id)


