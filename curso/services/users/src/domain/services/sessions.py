from src.domain.repositories.sessions import SessionsRepository
from src.libs.sessions import Session


class SessionsService:
    def __init__(self, repo: SessionsRepository):
        self.repo = repo

    def generate(self, user_id: int) -> Session:
        return self.repo.generate(user_id)

    def reject(self, access_token: str, refresh_token: str) -> None:
        return self.repo.reject(access_token, refresh_token)
