import httpx

from .dtos import Session
from src.infra.logger import log


class Client:
    base_url: str
    api_key: str

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key


    def generate(self, user_id: int) -> Session:
        url = f'{self.base_url}/'

        payload = {
            'user_id': user_id
        }

        headers = {
            "X-Api-Key": self.api_key
        }

        log.debug("generating session", user_id=user_id, url=url, headers=headers, payload=payload)

        response = httpx.post(url, json=payload, headers=headers, follow_redirects=True)
        response.raise_for_status()

        return Session(**response.json())

    def reject(self, access_token: str, refresh_token: str) -> None:
        url = f'{self.base_url}/reject'

        headers = {
            "X-Api-Key": self.api_key,
            "Authorization": f'Bearer {access_token}',
            "Refresh-Token": refresh_token
        }

        log.debug("rejecting session", url=url, headers=headers)

        response = httpx.delete(url, headers=headers, follow_redirects=True)

        if response.status_code == 401:
            log.warning("Invalid token", url=url, headers=headers)
            return

        response.raise_for_status()
