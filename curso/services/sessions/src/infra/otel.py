from fastapi import FastAPI
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry import trace, metrics

from .environment import envs

# Ensure OTEL_COLLECTOR_URL is set correctly
OTEL_COLLECTOR_URL = envs.get("OTEL_COLLECTOR_URL", "http://otel-collector:4317")

SERVICE_NAME = envs.get("SERVICE_NAME", "fastapi-app")

# Configure OpenTelemetry tracing
resource = Resource(attributes={"service.name": SERVICE_NAME})
tracer_provider = TracerProvider(resource=resource)

# Ensure the OTLP exporter is set to the correct endpoint
otlp_exporter = OTLPSpanExporter(endpoint=OTEL_COLLECTOR_URL, insecure=True)

# Add the span processor
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# Ensure tracer_provider is set globally
trace.set_tracer_provider(tracer_provider)

# Configure OpenTelemetry metrics
prometheus_reader = PrometheusMetricReader()
otlp_metric_exporter = OTLPMetricExporter(endpoint=OTEL_COLLECTOR_URL, insecure=True)
periodic_reader = PeriodicExportingMetricReader(otlp_metric_exporter)

meter_provider = MeterProvider(
    metric_readers=[prometheus_reader, periodic_reader],
    resource=resource
)

metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(SERVICE_NAME)


def instrument_app(app: FastAPI):
    FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider)
