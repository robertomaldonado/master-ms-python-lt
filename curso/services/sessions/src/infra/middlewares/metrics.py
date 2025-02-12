import time

from starlette.middleware.base import BaseHTTPMiddleware
from src.infra.metrics import REQUEST_COUNT, REQUEST_LATENCY
from src.infra.environment import envs

STAGE = envs.get("STAGE", "local")

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        latency_ms = duration * 1000

        REQUEST_COUNT.add(1, {
            "method": request.method,
            "endpoint": request.url.path,
            "http_status": response.status_code,
            "stage": STAGE,
        })

        REQUEST_LATENCY.record(latency_ms, {
            "method": request.method,
            "endpoint": request.url.path,
            "stage": STAGE,
        })

        return response