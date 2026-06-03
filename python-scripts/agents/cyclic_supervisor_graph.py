import logging
from typing import TypedDict

logger = logging.getLogger(__name__)

class GraphState(TypedDict):
    tenant_id: str
    lead_payload: dict
    missing_fields: list
    iteration_count: int
    routing_status: str

class CyclicSupervisorGraph:
    """
    Stateful Graph-Based Agentic Orchestrator.
    Replaces fragile linear pipelines with a resilient, cyclic state machine. 
    Iteratively routes B2B data through research and validation nodes until 
    strict schema criteria are satisfied, preventing incomplete CRM injections.
    """
    def __init__(self, max_cyclic_iterations: int = 3):
        self.max_iterations = max_cyclic_iterations

    def get_supervisor_guardrail_prompt(self) -> str:
        logger.debug("Generating deterministic 6-Component routing instructions...")
        
        return """
        [ROLE]: Principal Data Validation Supervisor.
        [TASK]: Evaluate the state of the B2B lead payload and determine the next cyclic routing node.
        [INPUT]: {current_graph_state}
        [OUTPUT]: A strict routing string: 'ROUTE_RESEARCH', 'ROUTE_DLQ', or 'ROUTE_CRM_INJECTION'.
        [CONSTRAINTS]: Output exactly one string. You must route to CRM ONLY if missing_fields is empty.
        [CAPABILITIES]: Complex schema validation and autonomous cyclic routing logic.
        """

    def evaluate_and_route(self, current_state: GraphState) -> str:
        logger.info(f"Evaluating Graph State: Iteration {current_state['iteration_count']} for tenant {current_state['tenant_id']}")
        
        if not current_state["missing_fields"] and current_state["routing_status"] == "VALIDATED":
            logger.info("Terminal Node Reached: Payload structurally perfect. Routing to CRM Injection.")
            return "ROUTE_CRM_INJECTION"
            
        if current_state["iteration_count"] >= self.max_iterations:
            logger.warning("Cyclic iteration cap breached. Routing payload to Dead Letter Queue (DLQ).")
            return "ROUTE_DLQ"
            
        logger.info(f"Missing fields detected: {current_state['missing_fields']}. Routing cyclic execution back to Research Node.")
        # State mutation will occur in the target node before looping back to supervisor
        return "ROUTE_RESEARCH"
