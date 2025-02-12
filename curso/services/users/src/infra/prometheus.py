from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_request_count", "App Request Count", ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds", "Request latency", ["method", "endpoint"]
)

