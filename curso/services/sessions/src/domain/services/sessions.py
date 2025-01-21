from datetime import datetime, timezone
from typing import Tuple

import jwt
from dateutil.relativedelta import relativedelta

from src.domain.filters.filters import Filters
from src.domain.repositories.sessions import SessionRepository
from src.models import Session
from src.infra.environment import envs
from src.infra.logger import log


class SessionService:
    def __init__(self, repo: SessionRepository):
        self.repo = repo

    def generate(self, user_id: int) -> Session:
        now = datetime.now(tz=timezone.utc)

        access_token = self._generate_access_token(user_id, now)
        refresh_token = self._generate_refresh_token(access_token)
        expires_at = self._get_expiration_date(now)

        return self.repo.create(
            user_id=user_id,
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at
        )

    def refresh(self, access_token: str, refresh_token: str) -> Session:
        session, user_id = self._get_session(access_token, refresh_token)

        now = datetime.now(tz=timezone.utc)

        if session.expires_at.replace(tzinfo=timezone.utc) < now:
            raise ValueError("Expired Refresh Token")

        access_token = self._generate_access_token(user_id, now)
        refresh_token = self._generate_refresh_token(access_token)
        new_expires_at = self._get_expiration_date(now)

        return self.repo.update(session.id, access_token=access_token, expires_at=new_expires_at, refresh_token=refresh_token)


    def reject(self, access_token: str, refresh_token: str) -> bool:
        session, _ = self._get_session(access_token, refresh_token)
        self.repo.delete(session.id)

        return True

    def verify(self, access_token: str) -> bool:
        try:
            jwt.decode(access_token, envs.get("JWT_SECRET"), algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError as e:
            log.warning("Token expired", error=str(e))
            return False
        except Exception as e:
            log.error("Error while verifying token", error=str(e))
            raise e

    def global_reject(self, user_id: int) -> bool:
        # TODO: Implementar
        pass

    def _generate_access_token(self, user_id: int, now: datetime) -> str:
        payload = {
            "user_id": user_id,
            "exp": now + relativedelta(minutes=2),
            "iat": now
        }

        log.debug("Generating session", user_id=user_id, payload=payload)

        return jwt.encode(payload, envs.get("JWT_SECRET"), algorithm="HS256")

    def _generate_refresh_token(self, access_token: str) -> str:
        payload_refresh = {
            "access_token": access_token
        }

        return jwt.encode(payload_refresh, envs.get("JWT_SECRET"), algorithm="HS256")

    def _get_expiration_date(self, now: datetime) -> datetime:
        return now + relativedelta(days=7)

    def _get_session(self, access_token: str, refresh_token: str) -> Tuple[Session, int]:
        decoded_refresh = jwt.decode(refresh_token, envs.get("JWT_SECRET"), algorithms=["HS256"])

        if access_token != decoded_refresh.get("access_token"):
            raise ValueError("Invalid refresh token")

        payload = jwt.decode(access_token, envs.get("JWT_SECRET"), algorithms=["HS256"], options={"verify_signature": False})

        user_id = payload.get("user_id")

        session = self.repo.find(filters=Filters(
            user_id=user_id,
            access_token=access_token,
            refresh_token=refresh_token
        ))

        if not session:
            raise ValueError("Invalid session")

        return session, user_id
