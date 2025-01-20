from typing import Dict, Any

from src.models.base import Base

from sqlalchemy import Column, Integer, String, DateTime, func


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    access_token = Column(String, nullable=False, index=True)
    refresh_token = Column(String, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Session(id={self.id}, user_id={self.user_id}, token={self.token})>"

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Session':
        self = Session()

        for field in data:
            if hasattr(self, field):
                setattr(self, field, data[field])

        return self

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at.strftime("%m/%d/%Y-%H:%M:%S"),
            "created_at": self.created_at.strftime("%m/%d/%Y-%H:%M:%S"),
            "updated_at": self.updated_at.strftime("%m/%d/%Y-%H:%M:%S"),
            "deleted_at": self.deleted_at.strftime("%m/%d/%Y-%H:%M:%S") if self.deleted_at else None
        }
