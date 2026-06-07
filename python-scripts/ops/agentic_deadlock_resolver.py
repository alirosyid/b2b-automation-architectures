import time
import logging
from collections import defaultdict
from typing import Dict, List

logger = logging.getLogger(__name__)

class AgenticDeadlockResolver:
    """
    Multi-Agent Swarm Resilience.
    Monitors stateful transitions within cyclical agent architectures. 
    Detects temporal freezing and circular logic dependencies (Deadlocks), 
    autonomously injecting a supervisor override to force orchestration progression.
    """
    def __init__(self, timeout_threshold_sec: int = 45):
        self.threshold = timeout_threshold_sec
        self.agent_states: Dict[str, dict] = defaultdict(dict)

    def log_agent_wait_state(self, agent_id: str, waiting_on_agent_id: str):
        self.agent_states[agent_id] = {
            "waiting_on": waiting_on_agent_id,
            "timestamp": time.time()
        }

    def detect_and_resolve_deadlocks(self) -> List[str]:
        current_time = time.time()
        resolved_agents = []
        
        for agent_id, state in list(self.agent_states.items()):
            target_agent = state["waiting_on"]
            time_waiting = current_time - state["timestamp"]
            
            # Check for circular dependency: A waiting on B, B waiting on A
            target_state = self.agent_states.get(target_agent, {})
            is_circular = target_state.get("waiting_on") == agent_id
            
            if is_circular or time_waiting > self.threshold:
                logger.critical(f"DEADLOCK DETECTED: Agent {agent_id} stalled. Executing forced supervisor override.")
                self.agent_states.pop(agent_id, None)
                self.agent_states.pop(target_agent, None)
                resolved_agents.extend([agent_id, target_agent])
                
        return resolved_agents
