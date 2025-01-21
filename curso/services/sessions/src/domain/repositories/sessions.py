from datetime import datetime
from typing import List

from sqlalchemy.orm import Session as DBSession
from sqlalchemy.sql import update

from src.domain.filters.filters import Filters
from src.models.session import Session


class SessionRepository:
    def __init__(self, db: DBSession):
        self.db = db

    def create(self, user_id: int, access_token: str, refresh_token: str, expires_at: datetime) -> Session:
        session = Session(
            user_id=user_id,
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at
        )

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def delete(self, session_id: int) -> Session:
        session = self.db.query(Session).filter(Session.id == session_id).first()

        if not session:
            raise ValueError("Session not found")

        if session.deleted_at:
            return session

        session.deleted_at = datetime.now()

        self.db.commit()
        self.db.refresh(session)

        return session

    def delete_many(self, filters: Filters) -> bool:
        query = update(Session)
        query = filters.apply(query)

        query.

        self.db.commit()

        return True

    def search(self, filters: Filters, limit: int = 10, offset: int = 0) -> List[Session]:
        query = self.db.query(Session)
        query = filters.apply(query)

        query = query.filter(Session.deleted_at.is_(None)) \
            .order_by(Session.id).group_by(Session.user_id)

        return query.limit(limit).offset(offset).all()


    def find(self, filters: Filters) -> Session:
        query = self.db.query(Session)
        query = filters.apply(query)

        query = query.filter(Session.deleted_at.is_(None))

        return query.first()

    def update(self, id: int,
        access_token: str | None = None,
        refresh_token: str | None = None,
        expires_at: datetime | None = None,
    ) -> Session:
        session = self.db.query(Session).filter(Session.id == id).first()

        if not session:
            raise ValueError("Session not found")

        if access_token:
            session.access_token = access_token

        if refresh_token:
            session.refresh_token = refresh_token

        if expires_at:
            session.expires_at = expires_at

        self.db.commit()
        self.db.refresh(session)

        return session
