import logging
from datetime import datetime, timezone

class TemporalDecayEngine:
    """
    PORTFOLIO SHOWCASE: GraphRAG Temporal Pruning.
    Applies mathematical half-life decay to aging enterprise knowledge nodes.
    """
    def __init__(self, half_life_days: int = 30):
        self.half_life = half_life_days

    def apply_decay_dry_run(self, graph_edges: list[dict]):
        logging.info("[PORTFOLIO MOCK] Scanning GraphRAG edges for temporal decay...")
        
        current_time = datetime(2026, 6, 10, 9, 13, 58, tzinfo=timezone.utc)
        
        for edge in graph_edges:
            days_old = (current_time - edge.get("last_verified_date")).days
            
            if days_old > self.half_life:
                edge["confidence_score"] *= 0.5  # Decay the weight by half
                logging.info(f"[DATA ENG MOCK] Edge {edge['id']} decayed. New score: {edge['confidence_score']}")
                
                if edge["confidence_score"] < 0.1:
                    logging.warning(f"[DATA ENG MOCK] Edge {edge['id']} falls below threshold. Queued for garbage collection.")
