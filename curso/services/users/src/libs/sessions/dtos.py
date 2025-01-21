from datetime import datetime

from pydantic import BaseModel


class Session(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
    expires_at: datetime

    def __repr__(self):
        return f'<Session user_id={self.user_id} access_token={self.access_token} refresh_token={self.refresh_token} expires_at={self.expires_at}>'
