import json

from fastapi import Request, Response

from src.infra.environment import envs

from src.infra.logger import log


async def api_key(req: Request, next):
    key = envs.get("API_KEY")

    if key == "":
        return await next(req)

    log.debug("Verifying API key", auth_header=req.headers.get("X-Api-Key"))

    if req.headers.get("X-Api-Key") != key:
        return Response(
            status_code=403,
            content=json.dumps({"message": "Unauthorized access"}),
            headers={"Content-Type": "application/json"}
        )

    return await next(req)
