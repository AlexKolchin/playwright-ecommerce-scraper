from abc import ABC, abstractmethod
import logging
from typing import List, Optional
from playwright.async_api import Page
from pydantic import BaseModel


class BaseScraper(ABC):
    """Abstract base class for all e-commerce scrapers."""

    def __init__(self, base_url: str, headless: bool = True):
        self.base_url = base_url
        self.headless = headless
        # Dynamically retrieve logger with the concrete subclass name
        self.logger = logging.getLogger(self.__class__.__name__)

    async def fetch_page(self, page: Page, url: str) -> Optional[str]:
        """Fetches page HTML content with structured error handling and logging."""
        self.logger.info(f"Navigating to URL: {url}")

        try:
            response = await page.goto(url, wait_until="networkidle", timeout=30000)

            if not response:
                self.logger.error(f"No response received from {url}")
                return None

            status = response.status
            if status == 200:
                content = await page.content()
                self.logger.info(
                    f"Successfully fetched {url} | Status: {status} | Size: {len(content)} bytes"
                )
                return content
            elif status in (401, 403):
                self.logger.warning(
                    f"Access restricted for {url} | Status: {status} (Check Proxy/Headers/Captcha)"
                )
            else:
                self.logger.warning(
                    f"Unexpected status code for {url} | Status: {status}"
                )

            return None

        except Exception as exc:
            self.logger.exception(f"Unhandled exception while fetching {url}: {exc}")
            return None

    @abstractmethod
    async def parse(self, page: Page) -> List[BaseModel]:
        """Abstract method to parse data from a specific target site."""
        pass
