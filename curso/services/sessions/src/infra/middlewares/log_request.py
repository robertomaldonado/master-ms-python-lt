import json

from datetime import datetime

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import StreamingResponse

from src.infra.logger import log

class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next):
        path = req.url.path
        query_params = {}
        headers = {}
        method = req.method

        for header, value in req.headers.items():
            headers[header] = value

        for query_param, value in req.query_params.items():
            query_params[query_param] = value

        # if content-type is application/json
        if "application/json" in headers.get("content-type", ""):
            body = await req.json()
        else:
            body = await req.body()
            body = {"raw": body.decode("utf-8")}

        start = datetime.now()
        res = await call_next(req)
        end = datetime.now()

        latency = end - start

        # convert to milliseconds from timedelta
        latency_ms = latency.total_seconds() * 1000

        async def response_body_generator():
            response_body = b""
            async for chunk in res.body_iterator:
                response_body += chunk
                yield chunk  # Send chunk to the client

            try:
                res_json = json.loads(response_body.decode("utf-8"))
            except json.JSONDecodeError:
                res_json = {"raw": response_body.decode("utf-8")}

            if 200 <= res.status_code < 300:
                log.info("handled request",
                    path=path,
                    query_params=query_params,
                    headers=headers,
                    method=method,
                    req_body=body,
                    latency=latency_ms,
                    status_code=res.status_code,
                    res_body=res_json,
                )
            else:
                log.error("handled request",
                    path=path,
                    query_params=query_params,
                    headers=headers,
                    method=method,
                    req_body=body,
                    latency=latency_ms,
                    status_code=res.status_code,
                    res_body=res_json,
                )

        return StreamingResponse(response_body_generator(), status_code=res.status_code, headers=dict(res.headers), media_type=res.media_type)
