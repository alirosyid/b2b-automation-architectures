import json
from datetime import datetime
from typing import Dict, Any

class GraphRAGDriftSync:
    def __init__(self, baseline_schema: set):
        self.baseline = baseline_schema

    def synchronize(self, incoming_payload: Dict[str, Any]) -> Dict[str, Any]:
        processed_data = {"_metadata_unmapped": {}}
        incoming_keys = set(incoming_payload.keys())
        
        drift_detected = incoming_keys - self.baseline
        
        for key, value in incoming_payload.items():
            if key in self.baseline:
                processed_data[key] = value
            else:
                processed_data["_metadata_unmapped"][key] = value
                
        processed_data["sync_timestamp"] = datetime.now().isoformat()
        return processed_data

# Expected baseline fields
baseline = {"company_name", "annual_revenue", "industry"}
sync_engine = GraphRAGDriftSync(baseline)
new_webhook_data = {"company_name": "TechCorp USA", "annual_revenue": "50M", "new_social_field": "twitter.com/techcorp"}

print(json.dumps(sync_engine.synchronize(new_webhook_data), indent=2))
