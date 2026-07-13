import time

def build_temporal_edge(source_entity, target_entity, relationship, valid_from, valid_to=None):
    print(f"[RAG Ops] Forging temporal relationship: {source_entity} -> {relationship} -> {target_entity}")
    
    temporal_edge = {
        "source": source_entity,
        "target": target_entity,
        "relation": relationship,
        "metadata": {
            "valid_from": valid_from,
            "valid_to": valid_to or "present",
            "is_active": valid_to is None
        }
    }
    
    # Resolves AI queries like "What was our SLA response time for this client in 2025?"
    print(f"[+] Temporal graph edge established. Historical reasoning capability expanded.")
    return temporal_edge

if __name__ == "__main__":
    build_temporal_edge("Enterprise_X", "SLA_Tier_1", "contracted_to", valid_from="2025-01-01", valid_to="2025-12-31")
    build_temporal_edge("Enterprise_X", "SLA_Tier_Premium", "contracted_to", valid_from="2026-01-01")
