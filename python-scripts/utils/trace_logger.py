import uuid
import logging

class DistributedTracer:
    """
    Generates and propagates trace IDs across n8n workflows and Python microservices.
    Crucial for debugging complex, multi-stage automation failures.
    """
    @staticmethod
    def generate_trace_id() -> str:
        return f"req_{uuid.uuid4().hex[:12]}"

    @staticmethod
    def log_with_trace(logger_instance: logging.Logger, trace_id: str, message: str, level: str = "info"):
        formatted_message = f"[TraceID: {trace_id}] {message}"
        if level == "info":
            logger_instance.info(formatted_message)
        elif level == "error":
            logger_instance.error(formatted_message)
