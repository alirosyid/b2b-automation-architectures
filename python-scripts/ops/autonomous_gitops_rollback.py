import os
import subprocess
import logging
from collections import deque
import time

logger = logging.getLogger(__name__)

class AutonomousGitOpsRollback:
    """
    Self-Healing Infrastructure Operations.
    Continuously monitors pipeline error telemetry post-deployment. Autonomously 
    executes hard Git reverts to the last known stable state if catastrophic 
    regression failures are detected, guaranteeing enterprise service availability.
    """
    def __init__(self, failure_threshold: float = 0.30):
        self.failure_threshold = failure_threshold
        self.recent_executions = deque(maxlen=100)
        self.deployment_time = time.time()

    def log_execution(self, is_success: bool):
        self.recent_executions.append(is_success)
        self._evaluate_health()

    def _evaluate_health(self):
        # Only evaluate if we have a sufficient sample size recently after a deploy
        if len(self.recent_executions) == 100 and (time.time() - self.deployment_time) < 3600:
            failure_rate = 1.0 - (sum(self.recent_executions) / 100.0)
            
            if failure_rate > self.failure_threshold:
                logger.critical(f"CRITICAL REGRESSION DETECTED: Failure rate at {failure_rate * 100}%. Initiating GitOps Rollback.")
                self._execute_hard_revert()

    def _execute_hard_revert(self):
        try:
            # Revert to the previous commit locally and restart application services
            subprocess.run(["git", "reset", "--hard", "HEAD~1"], check=True)
            logger.info("Git repository reverted to last stable commit. Initiating service restart sequence.")
            # Production: Trigger systemd restart or Kubernetes pod deletion
        except subprocess.CalledProcessError as e:
            logger.error(f"Autonomous rollback failed. Manual SRE intervention required: {e}")
