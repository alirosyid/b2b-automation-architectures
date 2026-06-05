import logging

logger = logging.getLogger(__name__)

class ROICalculator:
    """
    Tracks and logs the business value generated per automation run.
    """
    @staticmethod
    def log_execution_value(workflow_name: str, items_processed: int, manual_minutes_per_item: int = 5, hourly_rate: float = 25.0):
        hours_saved = (items_processed * manual_minutes_per_item) / 60.0
        money_saved = hours_saved * hourly_rate
        logger.info(
            f"ROI Metrics - Workflow: {workflow_name} | "
            f"Items: {items_processed} | "
            f"Hours Saved: {hours_saved:.2f} | "
            f"Value Generated: ${money_saved:.2f}"
        )
        return {"hours_saved": hours_saved, "money_saved": money_saved}
