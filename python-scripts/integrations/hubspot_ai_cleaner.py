import requests
import os

def merge_crm_duplicates(primary_id, secondary_id):
    url = f"https://api.hubapi.com/crm/v3/objects/contacts/merge"
    headers = {
        "Authorization": f"Bearer {os.getenv('HUBSPOT_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "primaryObjectId": primary_id,
        "objectIdToMerge": secondary_id
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Successfully merged contact {secondary_id} into {primary_id}")
    else:
        print("Merge failed:", response.text)

# Note: LLM fuzzy matching logic runs prior to this API call.
