import json
import time

class AgentTelemetry:
    """
    Captures the intermediate reasoning steps and latency of autonomous agents.
    Crucial for debugging 'black-box' LLM behavior in production environments.
    """
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.traces = []

    def log_step(self, step_name: str, input_data: str, output_data: str, duration_ms: int):
        trace = {
            "timestamp": time.time(),
            "agent": self.agent_name,
            "step": step_name,
            "payload_size": len(input_data),
            "latency_ms": duration_ms
        }
        self.traces.append(trace)
        # In production, this flushes to an APM tool like Datadog or LangSmith
        print(f"Telemetry logged: {json.dumps(trace)}")
