def get_openapi_metadata() -> dict:
    """
    Configuration for auto-generating interactive Swagger/Redoc documentation.
    Ensures enterprise IT teams can easily integrate with our AI microservices.
    """
    return {
        "title": "B2B AI Automation Engine API",
        "description": "Enterprise-grade endpoints for OCR, Data Enrichment, and Agentic Workflows.",
        "version": "2.0.0",
        "contact": {
            "name": "Ali Rosyid - Chief Architect",
            "url": "https://github.com/alirosyid",
        },
        "servers": [
            {"url": "https://api.production.internal", "description": "Production Cluster"},
            {"url": "http://localhost:8000", "description": "Local Development"}
        ]
    }
