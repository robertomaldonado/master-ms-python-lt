import time

from starlette.middleware.base import BaseHTTPMiddleware
from src.infra.prometheus import REQUEST_COUNT, REQUEST_LATENCY


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        method = request.method
        endpoint = request.url.path

        start_time = time.time()
        response = await call_next(request)
        latency = time.time() - start_time

        REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=response.status_code).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
        return response