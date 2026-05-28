import logging
from typing import List

logger = logging.getLogger(__name__)

class RBACToolInterceptor:
    """
    Zero-Trust Multi-Agent Security.
    Enforces Role-Based Access Control (RBAC) on agentic tool execution.
    Prevents unauthorized or compromised AI agents from escalating privileges 
    and executing destructive pipeline mutations.
    """
    def __init__(self, agent_role: str, allowed_scopes: List[str]):
        self.role = agent_role
        self.scopes = allowed_scopes

    def authorize_execution(self, requested_tool: str) -> bool:
        logger.debug(f"Intercepting tool execution request: {requested_tool} by {self.role}")
        
        # Verify if the tool falls within the agent's granted cryptographic scopes
        if not any(requested_tool.startswith(scope) for scope in self.scopes):
            logger.critical(f"SECURITY BREACH BLOCKED: Agent '{self.role}' attempted unauthorized tool access: {requested_tool}.")
            return False
            
        logger.info(f"Execution authorized. Agent '{self.role}' cleared for {requested_tool}.")
        return True
