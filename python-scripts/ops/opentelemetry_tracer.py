import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class OpenTelemetryTracer:
    """
    Enterprise Observability Architecture.
    Wraps critical AI and orchestration functions with OpenTelemetry-compatible 
    spans to track execution latency, pinpointing pipeline bottlenecks 
    and proving SLA compliance to B2B stakeholders.
    """
    @staticmethod
    def trace_execution(span_name: str, func: Callable, *args, **kwargs) -> Any:
        start_time = time.time()
        logger.info(f"[TRACE START] Initializing span: {span_name}")
        
        try:
            result = func(*args, **kwargs)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[TRACE END] Span '{span_name}' completed in {duration_ms:.2f}ms. Status: SUCCESS")
            return result
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[TRACE ERROR] Span '{span_name}' failed after {duration_ms:.2f}ms. Error: {e}")
            raise
