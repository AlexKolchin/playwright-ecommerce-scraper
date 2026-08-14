import asyncio
import logging
from playwright.async_api import async_playwright

from config.logger_config import setup_logging
from scrapers.catalog_scraper import CatalogScraper
from utils.file_manager import save_products_to_json


async def main():
    setup_logging(level=logging.INFO)
    logger = logging.getLogger("Main")

    target_url = "https://books.toscrape.com/"
    scraper = CatalogScraper(base_url=target_url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        logger.info("Starting extraction process across all pages...")

        # Scrape pages (set max_pages=5 for testing, or set to None for all pages
        all_products = await scraper.scrape_all_pages(
            page, target_url, max_pages=5
        )

        logger.info(f"Total products scraped: {len(all_products)}")

        # Save scraped dataset into JSON format
        save_products_to_json(all_products, "data/products.json")
        logger.info("Successfully saved products to 'data/products.json'")

        await browser.close()

if __name__ == "__main__":
        asyncio.run(main())