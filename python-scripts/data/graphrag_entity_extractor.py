import json

def extract_graph_entities(raw_text):
    print("[Data] Analyzing unstructured text for GraphRAG relationships...")
    
    # Mocking LLM extraction of nodes and edges
    graph_data = {
        "nodes": [
            {"id": "Automation Agency", "type": "Organization"},
            {"id": "HubSpot", "type": "Software"},
            {"id": "API Sync", "type": "Process"}
        ],
        "edges": [
            {"source": "Automation Agency", "target": "HubSpot", "relation": "integrates_with"},
            {"source": "API Sync", "target": "HubSpot", "relation": "updates_data_in"}
        ]
    }
    
    print(f"[+] Extracted {len(graph_data['nodes'])} nodes and {len(graph_data['edges'])} edges.")
    return json.dumps(graph_data, indent=2)

if __name__ == "__main__":
    mock_text = "The Automation Agency integrates with HubSpot to perform API Syncs."
    extract_graph_entities(mock_text)
