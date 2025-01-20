import os
from typing import Any

from structlog import get_logger, configure, processors, stdlib


SERVICE_NAME = os.environ.get("SERVICE_NAME", "fastapi-service")
STAGE = os.environ.get("STAGE", "local")


def config_prod_logger() -> Any:
    configure(
        processors=[
            processors.TimeStamper(fmt="iso"),  # Add ISO timestamp
            processors.JSONRenderer(),  # Render logs as JSON
        ],
    )


if STAGE != "local":
    config_prod_logger()

log = get_logger()
log = log.bind(service_name=SERVICE_NAME, stage=STAGE)
