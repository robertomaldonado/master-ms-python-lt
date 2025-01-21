from fastapi import HTTPException

from src.domain.filters.filters import Filters
from src.domain.services import UserService
from src.domain.services.sessions import SessionsService
from src.routes.dtos.session import LoginResponse, LogoutResponse
from src.infra.logger import log


class SessionsController:
    def __init__(self, srv_users: UserService, srv_sessions: SessionsService):
        self.srv_users = srv_users
        self.srv_sessions = srv_sessions

    def login(self, email: str, password: str) -> LoginResponse:
        user = self.srv_users.find(filters=Filters(email=email))

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        try:
            user.verify_password(password)
        except Exception as e:
            log.warning("Invalid password", user_id=user.id, email=user.email, error=str(e))
            raise HTTPException(status_code=401, detail="Invalid credentials")

        try:
            session = self.srv_sessions.generate(user.id)
        except Exception as e:
            log.error("Error while generating session", user_id=user.id, email=user.email, error=str(e))
            raise HTTPException(status_code=500, detail="Internal server error")

        return LoginResponse(
            user_id=session.user_id,
            access_token=session.access_token,
            refresh_token=session.refresh_token,
            expires_at=session.expires_at,
        )

    def logout(self, access_token: str, refresh_token: str) -> LogoutResponse:
        # TODO: Implement sessions service integration

        return LogoutResponse(message="Logged out")


