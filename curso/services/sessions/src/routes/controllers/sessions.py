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

        return self.srv_sessions.refresh(
            access_token=access_token,
            refresh_token=refresh_token
        )

    def reject(self, access_token: str, refresh_token: str) -> bool:
        if access_token == "" or refresh_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        # TODO: Implementar
        # decodificar refresh_token
        # verificar que el access_token sea igual al access_token del refresh_token
        # obtener user_id del access_token
        # buscar session en base de datos usando user_id, access_token y refresh_token con el metodo find
        # si no existe, retornar execpcion
        # borrar session de base de datos usas el repositorio (soft delete)
        pass

    def reject_global(self, access_token: str, refresh_token: str) -> bool:
        if access_token == "" or refresh_token == "":
            raise HTTPException(status_code=422, detail="Invalid token")

        # TODO: Implementar
        # decodificar refresh_token
        # verificar que el access_token sea igual al access_token del refresh_token
        # obtener user_id del access_token
        # buscar session en base de datos usando user_id, access_token y refresh_token con el metodo search
        # si no existe, retornar execpcion
        # borrar todas las sessiones usado el repositorio (soft delete)
        pass


