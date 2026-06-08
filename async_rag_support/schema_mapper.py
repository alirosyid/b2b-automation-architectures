def sync_graphrag_schema_drift(legacy_schema: dict, actual_schema: dict) -> dict:
    mapped_schema = {
        "orchestrator_metadata": {
            "audit_timestamp": "2026-06-08T13:57:35+07:00",
            "stateful_identity_resolution": "active",
            "drift_status": "detected_and_mapped"
        },
        "schema_relational_bridge": {
            "legacy_schema_version": legacy_schema.get("version", "unknown"),
            "actual_schema_version": actual_schema.get("version", "unknown"),
            "attribute_mapping": {}
        },
        "_metadata_unmapped": {
            "orphaned_legacy_attributes": [],
            "unrecognized_actual_attributes": []
        }
    }

    for key, value in actual_schema.items():
        if key not in legacy_schema and key != "version":
            mapped_schema["_metadata_unmapped"]["unrecognized_actual_attributes"].append({key: value})
            
    return mapped_schema
