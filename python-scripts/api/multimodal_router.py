import logging

logger = logging.getLogger(__name__)

class MultimodalIngestionRouter:
    """
    Dynamically analyzes incoming webhook payloads and routes them to the 
    appropriate AI processing engine based on MIME type.
    """
    @staticmethod
    def route_payload(mime_type: str, file_uri: str) -> str:
        if mime_type.startswith("image/") or mime_type == "application/pdf":
            logger.info(f"Visual payload detected ({mime_type}). Routing to Gemini Vision OCR.")
            return "gemini_vision_pipeline"
        elif mime_type == "audio/mpeg":
            logger.info("Audio payload detected. Routing to Whisper transcription engine.")
            return "whisper_audio_pipeline"
        else:
            logger.info("Standard text payload detected. Routing to Groq Llama-3 extractor.")
            return "groq_text_pipeline"
