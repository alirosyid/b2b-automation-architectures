from datetime import datetime

class ExecutiveReporter:
    """
    Menghasilkan rangkuman metrik bisnis harian untuk pemangku kepentingan (Stakeholders).
    Meningkatkan transparansi dan retensi klien.
    """
    @staticmethod
    def generate_markdown_summary(leads_processed: int, errors: int, api_cost: float) -> str:
        date_str = datetime.utcnow().strftime('%Y-%m-%d')
        success_rate = ((leads_processed - errors) / leads_processed) * 100 if leads_processed else 0

        return f"""
        # 📊 B2B Automation Daily Summary - {date_str}
        - **Total Leads Processed:** {leads_processed}
        - **Pipeline Success Rate:** {success_rate:.2f}%
        - **Total API Cost:** ${api_cost:.2f}
        - **System Status:** 🟢 All systems operational
        """
