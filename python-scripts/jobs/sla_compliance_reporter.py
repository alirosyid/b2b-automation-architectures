from datetime import datetime

class SLAReportGenerator:
    """
    Aggregates monthly telemetry to generate an automated, legally compliant 
    Service Level Agreement (SLA) report for B2B stakeholders.
    """
    @staticmethod
    def generate_monthly_report(client_name: str, uptime_pct: float, total_processed: int) -> str:
        month_str = datetime.utcnow().strftime('%B %Y')
        breach_status = "NONE" if uptime_pct >= 99.9 else "BREACH DETECTED"

        report = f"""
        # SLA Compliance Report: {client_name}
        **Billing Period:** {month_str}

        ## System Performance
        * **Guaranteed Uptime:** 99.90%
        * **Actual Uptime:** {uptime_pct:.2f}%
        * **SLA Violation:** {breach_status}

        ## Volume Metrics
        * **Total Automated Executions:** {total_processed}

        *Generated automatically by B2B Automation Engine.*
        """
        return report.strip()
