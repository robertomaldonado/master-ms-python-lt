import socket
import json
from structlog import get_logger, configure, processors, stdlib
from structlog.stdlib import LoggerFactory

from .environment import envs

SERVICE_NAME = envs.get("SERVICE_NAME", "users")
STAGE = envs.get("STAGE", "local")

LOGSTASH_HOST = envs.get("LOGSTASH_HOST", "")  # Logstash container name
LOGSTASH_PORT = envs.get_int("LOGSTASH_PORT", 0)  # Logstash TCP port

# Configure Logstash logging
def send_to_logstash(logger, method_name, event_dict):
    if not LOGSTASH_HOST or not LOGSTASH_PORT:
        return event_dict  # Structlog expects event_dict to be returned

    try:
        logstash_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Use SOCK_DGRAM for UDP
        logstash_socket.connect((LOGSTASH_HOST, LOGSTASH_PORT))
        logstash_socket.sendall(json.dumps(event_dict).encode("utf-8") + b"\n")
        logstash_socket.close()
    except Exception as e:
        print(f"Logstash connection error: {e}")  # Fallback to console logging

    return event_dict  # Structlog requires the event_dict to be returned

# Configure Structlog
configure(
    processors=[
        stdlib.add_log_level,
        processors.TimeStamper(fmt="iso"),
        processors.JSONRenderer(),
        send_to_logstash,  # Send logs to Logstash
    ],
    logger_factory=LoggerFactory(),
)

log = get_logger()
log = log.bind(service_name=SERVICE_NAME, stage=STAGE)
