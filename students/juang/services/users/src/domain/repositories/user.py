from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import Session

from src.models.user import User
from src.domain.filters.filters import Filters


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, username: str, password: str, app_version: Optional[str] = None) -> User:
        user = User(
            email=email,
            username=username,
            password=password,
            app_version=app_version
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update(self, user_id: int, email:Optional[str], username:Optional[str], app_version:Optional[str]) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()

        if email:
            user.email = email
        if username:
            user.username = username
        if app_version:
            user.app_version = app_version

        self.db.commit()
        self.db.refresh(user)

        return user

    def delete(self, user_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()

        if user.deleted_at:
            return user

        user.deleted_at = datetime.now()

        self.db.commit()
        self.db.refresh(user)

        return user

    def get(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def list_all(self) -> List[User]:
        return self.db.query(User).order_by(User.id).all()

    def count(self, filters: Filters) -> int:
        query = self.db.query(User)
        query = filters.apply(query)

        return query.count()

    def search(self, filters: Filters, limit: int = 10, offset: int = 0) -> List[User]:
        query = self.db.query(User)
        query = filters.apply(query)

        query = query.order_by(User.id)

        return query.limit(limit).offset(offset).all()
