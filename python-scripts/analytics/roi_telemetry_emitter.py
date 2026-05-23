import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ROITelemetryEmitter:
    """
    Executive Business Intelligence (BI) Integration.
    Emits real-time, standardized JSON metrics for every successful automation loop.
    Designed to feed directly into Grafana/Tableau dashboards, proving exact 
    financial ROI (hours saved, API costs, leads generated) to B2B stakeholders.
    """
    # Estimated cost of a human employee executing this task manually
    MANUAL_LABOR_COST_PER_TASK = 2.50 

    @classmethod
    def emit_success_metric(cls, task_name: str, execution_time_ms: int, api_cost_usd: float):
        savings = cls.MANUAL_LABOR_COST_PER_TASK - api_cost_usd

        telemetry_payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "metric_type": "roi_event",
            "task": task_name,
            "latency_ms": execution_time_ms,
            "api_cost_usd": api_cost_usd,
            "net_savings_usd": round(savings, 4)
        }

        # Print to stdout for log aggregators (e.g., Datadog, ELK stack)
        print(f"BI_TELEMETRY_EMIT: {json.dumps(telemetry_payload)}")
