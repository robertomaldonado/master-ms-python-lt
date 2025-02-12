from .otel import meter


REQUEST_COUNT = meter.create_counter(
    "http_requests_total",
    description="Total number of HTTP requests"
)

REQUEST_LATENCY = meter.create_histogram(
    "http_request_latency",
    description="HTTP request latency",
    unit="ms"
)