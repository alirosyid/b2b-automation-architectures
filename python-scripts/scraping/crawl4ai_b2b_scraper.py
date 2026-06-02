import asyncio
import logging
from crawl4ai import AsyncWebCrawler

logger = logging.getLogger(__name__)

class Crawl4AIStealthScraper:
    """
    Asynchronous Web Extraction Node.
    Utilizes Crawl4AI to stealthily navigate enterprise domains, bypass JS challenges, 
    and extract raw DOM structures into LLM-optimized Markdown for downstream enrichment.
    """
    @staticmethod
    async def extract_markdown(target_url: str) -> str:
        logger.info(f"Deploying Crawl4AI to extract domain: {target_url}")
        
        async with AsyncWebCrawler(verbose=False) as crawler:
            result = await crawler.arun(
                url=target_url,
                bypass_cache=True,
                word_count_threshold=10
            )
            
            if result.success:
                logger.info(f"Extraction successful. Recovered {len(result.markdown)} characters of Markdown.")
                return result.markdown
            else:
                logger.error(f"Crawl4AI extraction failed for {target_url}.")
                return ""
