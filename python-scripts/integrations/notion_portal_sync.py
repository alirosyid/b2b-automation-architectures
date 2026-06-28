def sync_status_to_notion(client_id, workflow_name, status):
    print(f"[Integrations] Connecting to Notion API for client portal: {client_id}")
    
    # Mock Notion page ID mapping
    notion_pages = {"ENT-001": "notion_page_x9f8", "ENT-002": "notion_page_b2c4"}
    page_id = notion_pages.get(client_id)
    
    if not page_id:
        print(f"[!] Error: No Notion portal mapped for {client_id}.")
        return False
        
    status_icon = "🟢" if status == "Success" else "🔴"
    print(f"[Integrations] Updating block in {page_id} -> {workflow_name}: {status_icon} {status}")
    
    return True

if __name__ == "__main__":
    sync_status_to_notion("ENT-001", "Lead Enrichment Pipeline", "Success")
    sync_status_to_notion("ENT-001", "Salesforce Sync", "Failed - Rate Limit")
