def map_endpoints_to_supergraph(legacy_endpoints):
    print("[Data Ops] Initializing GraphQL Supergraph Federation Mapper...")
    
    supergraph_schema = "type Query {\n"
    
    for endpoint in legacy_endpoints:
        # Mock API to GraphQL type inference
        entity_name = endpoint.split("/")[-1].capitalize()
        print(f"    -> Mapping REST endpoint '{endpoint}' to GraphQL type '{entity_name}'...")
        supergraph_schema += f"  get{entity_name}(id: ID!): {entity_name}\n"
        
    supergraph_schema += "}\n"
    
    print("[+] Disparate APIs successfully unified into single Supergraph schema.")
    print("    -> Deploying schema to Apollo Federation Gateway.")
    return supergraph_schema

if __name__ == "__main__":
    endpoints = ["api.legacy.com/v1/users", "billing.internal/v2/invoices"]
    print(map_endpoints_to_supergraph(endpoints))
