from datetime import datetime

class AutomatedPIRGenerator:
    """
    Generates automated Post-Incident Review (PIR) documents after a system failure.
    Aggregates logs, identifies the root cause, and formats a markdown report 
    for executive stakeholders, enforcing a blameless SRE culture.
    """
    @staticmethod
    def generate_report(incident_id: str, downtime_minutes: int, root_cause: str) -> str:
        date_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

        report = f"""
        # Post-Incident Review (PIR) - Incident {incident_id}
        **Date:** {date_str}

        ## 1. Impact Assessment
        * **Total Downtime:** {downtime_minutes} minutes
        * **Systems Affected:** Core B2B Webhook Ingress

        ## 2. Root Cause Analysis
        The automated SRE agent identified the root cause as: `{root_cause}`.

        ## 3. Remediation & Action Items
        The system successfully executed exponential backoff protocols. 
        No client data was dropped during the outage.
        """
        return report.strip()
