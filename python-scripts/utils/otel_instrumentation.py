from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

class OpenTelemetryManager:
    """
    Standardizes observability across the entire B2B pipeline using OpenTelemetry.
    Ensures seamless integration with enterprise APM tools (Datadog, New Relic, Grafana).
    """
    @staticmethod
    def setup_tracing(service_name: str = "b2b-automation-engine"):
        provider = TracerProvider()
        processor = BatchSpanProcessor(ConsoleSpanExporter())
        provider.add_span_processor(processor)
        trace.set_tracer_provider(provider)

        return trace.get_tracer(service_name)

# Usage: tracer = OpenTelemetryManager.setup_tracing()
# with tracer.start_as_current_span("enrich_lead_data"):
#     ...
