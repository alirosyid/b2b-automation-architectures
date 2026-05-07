import json
from datetime import datetime

class ROIDashboardExporter:
    """
    Mengekspor metrik penghematan otomatisasi ke format yang siap diserap
    oleh alat BI (Business Intelligence) seperti Google Data Studio atau Looker.
    """
    @staticmethod
    def export_daily_metrics(tasks_automated: int, avg_manual_cost: float, api_cost: float):
        gross_savings = tasks_automated * avg_manual_cost
        net_roi = gross_savings - api_cost

        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "metric_type": "daily_roi_summary",
            "gross_savings_usd": gross_savings,
            "api_expense_usd": api_cost,
            "net_business_value_usd": net_roi
        }
        # In production, this pushes to a BigQuery or Postgres BI table
        return json.dumps(payload)
