from typing import Any

from structlog import get_logger, configure, processors

from .environment import envs


SERVICE_NAME = envs.get("SERVICE_NAME", "sessions")
STAGE = envs.get("STAGE", "dev")


def config_prod_logger() -> Any:
    configure(
        processors=[
            processors.TimeStamper(fmt="iso"),  # Add ISO timestamp
            processors.JSONRenderer(),  # Render logs as JSON
        ],
    )


if STAGE != "dev":
    config_prod_logger()

log = get_logger()
log = log.bind(service_name=SERVICE_NAME, stage=STAGE)
