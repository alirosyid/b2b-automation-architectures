import logging
from typing import List

logger = logging.getLogger(__name__)

class IAMPermissionResolver:
    """
    Zero-Trust Tool Execution Gatekeeper.
    Verifies that an autonomous agent possesses the explicit cryptographic 
    role-based access control (RBAC) permissions before allowing it to trigger 
    high-stakes external APIs (e.g., modifying CRM records).
    """
    def __init__(self, agent_role: str, granted_scopes: List[str]):
        self.role = agent_role
        self.scopes = granted_scopes

    def authorize_tool_call(self, requested_tool: str) -> bool:
        if requested_tool not in self.scopes:
            logger.critical(f"IAM Violation: Agent '{self.role}' attempted unauthorized execution of '{requested_tool}'.")
            return False

        logger.info(f"IAM Authorization passed. Agent '{self.role}' cleared for '{requested_tool}'.")
        return True
