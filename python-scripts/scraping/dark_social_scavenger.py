import re

class DarkSocialScavenger:
    def __init__(self, target_keywords):
        self.target_keywords = target_keywords

    def scan_message_stream(self, username, message_content):
        message_lower = message_content.lower()
        
        for keyword in self.target_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', message_lower):
                print(f"[Lead Capture] Intent detected from {username}: '{message_content}'")
                return {"user": username, "intent_keyword": keyword, "action": "route_to_nurture"}
                
        return None

if __name__ == "__main__":
    scavenger = DarkSocialScavenger(["zapier limit", "manual data entry", "api timeout"])
    scavenger.scan_message_stream("DevOpsLead", "We keep hitting our Zapier limit, it's getting too expensive.")
