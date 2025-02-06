import json

from fastapi import Request, Response

from src.infra.environment import envs


async def api_key(req: Request, next):
    if ".health" in req.url.path:
        return await next(req)

    key = envs.get("API_KEY")

    if key == "":
        return await next(req)

    if req.headers.get("X-Api-Key") != key:
        return Response(
            status_code=403,
            content=json.dumps({"message": "Unauthorized access"}),
            headers={"Content-Type": "application/json"}
        )

    return await next(req)
