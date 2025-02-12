import json

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.infra.environment import envs


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if self._should_skip(request):
            return await call_next(request)

        key = envs.get("API_KEY")

        if key == "":
            return await call_next(request)

        if request.headers.get("X-Api-Key") != key:
            return Response(
                status_code=403,
                content=json.dumps({"message": "Unauthorized access"}),
                headers={"Content-Type": "application/json"}
            )

        return await call_next(request)

    @staticmethod
    def _should_skip(request: Request) -> bool:
        return ".health" in request.url.path or "prometheus/metrics" in request.url.path
