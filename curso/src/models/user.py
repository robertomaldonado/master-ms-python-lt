from sqlalchemy import Column, Integer, String, DateTime, func
from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    app_version = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, username={self.username})>"

    @staticmethod
    def from_dict(data: dict) -> 'User':
        self = User()

        for field in data:
            if hasattr(self, field):
                setattr(self, field, data[field])

        return self

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "app_version": self.app_version,
            "created_at": self.created_at.strftime("%m/%d/%Y-%H:%M:%S"),
            "updated_at": self.updated_at.strftime("%m/%d/%Y-%H:%M:%S"),
            "deleted_at": self.deleted_at.strftime("%m/%d/%Y-%H:%M:%S") if self.deleted_at else None
        }
