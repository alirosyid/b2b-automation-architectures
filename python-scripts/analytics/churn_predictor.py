import logging

logger = logging.getLogger(__name__)

class ChurnPredictor:
    """
    Revenue Protection Engine.
    Analyzes client workflow telemetry (execution frequency, error rates, data volume).
    If engagement drops below algorithmic thresholds, it flags the account as 
    'High Risk' for proactive intervention by Account Management.
    """
    @staticmethod
    def analyze_tenant_health(tenant_id: str, last_7_days_usage: int, error_rate_pct: float) -> dict:
        health_score = 100

        if last_7_days_usage == 0:
            health_score -= 50
        if error_rate_pct > 5.0:
            health_score -= 30

        status = "CRITICAL_RISK" if health_score < 40 else "HEALTHY"

        if status == "CRITICAL_RISK":
            logger.warning(f"CHURN ALERT: Tenant {tenant_id} health score dropped to {health_score}. Intervention required.")
            # Production: Trigger internal n8n webhook to Slack/CRM

        return {"tenant": tenant_id, "health_score": health_score, "status": status}
