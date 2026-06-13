import logging

class VectorDriftDetector:
    def __init__(self, drift_threshold: float = 0.15):
        self.threshold = drift_threshold

    def calculate_drift_dry_run(self, baseline_centroid: list, new_embedding: list) -> float:
        logging.info("[PORTFOLIO MOCK] Calculating cosine distance between baseline and new vectors.")
        
        # Mocking mathematical distance calculation
        mock_cosine_distance = 0.18 
        
        if mock_cosine_distance > self.threshold:
            logging.critical(f"[DATA MOCK] Severe Data Drift detected: {mock_cosine_distance}. Threshold: {self.threshold}")
            logging.info("[DATA MOCK] Recommendation: Trigger asynchronous Vector DB rebuild pipeline.")
            return mock_cosine_distance
            
        logging.info(f"[DATA MOCK] Embedding stable. Drift ({mock_cosine_distance}) is within safe operational limits.")
        return mock_cosine_distance
