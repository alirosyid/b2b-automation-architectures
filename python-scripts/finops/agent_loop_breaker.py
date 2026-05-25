import logging
from collections import defaultdict
import time

logger = logging.getLogger(__name__)

class AgentLoopBreaker:
    """
    Stateful FinOps Circuit Breaker.
    Tracks autonomous agent tool-calling patterns in real-time. Automatically 
    terminates agent execution if identical recursive API loops are detected, 
    preventing catastrophic LLM billing spikes.
    """
    def __init__(self, max_identical_calls: int = 3, time_window_sec: int = 60):
        self.max_calls = max_identical_calls
        self.window = time_window_sec
        self.execution_state = defaultdict(list)

    def authorize_tool_call(self, agent_id: str, tool_name: str, payload_hash: str) -> bool:
        current_time = time.time()
        state_key = f"{agent_id}_{tool_name}_{payload_hash}"

        # Clean up old state memory
        self.execution_state[state_key] = [
            t for t in self.execution_state[state_key] if current_time - t < self.window
        ]

        self.execution_state[state_key].append(current_time)

        if len(self.execution_state[state_key]) > self.max_calls:
            logger.critical(f"FINOPS ALERT: Infinite loop detected for agent {agent_id}. Terminating execution.")
            return False

        return True
