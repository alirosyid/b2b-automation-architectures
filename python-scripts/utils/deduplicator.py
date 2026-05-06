import hashlib

class LeadDeduplicator:
    """
    Mencegah entri data ganda ke dalam CRM klien menggunakan hashing kriptografi.
    Menghemat biaya penyimpanan HubSpot/Salesforce dan mencegah spam.
    """
    def __init__(self):
        self.seen_hashes = set()

    def is_duplicate(self, email: str, company: str) -> bool:
        unique_string = f"{email.lower().strip()}|{company.lower().strip()}"
        lead_hash = hashlib.sha256(unique_string.encode()).hexdigest()

        if lead_hash in self.seen_hashes:
            return True

        self.seen_hashes.add(lead_hash)
        return False
