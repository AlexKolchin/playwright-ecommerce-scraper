import asyncio
import logging
from playwright.async_api import async_playwright

from config.logger_config import setup_logging
from scrapers.catalog_scraper import CatalogScraper


async def main():
    setup_logging(level=logging.INFO)
    logger = logging.getLogger("Main")

    target_url = "https://books.toscrape.com/"
    scraper = CatalogScraper(base_url=target_url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        logger.info("Starting extraction process...")

        html_content = await scraper.fetch_page(page, target_url)

        if html_content:
            products = await scraper.parse(page)
            logger.info(
                f"Successfully parsed {len(products)} products from front page!"
            )

            print("\n--- Scraped Data Sample ---")
            for item in products[:3]:
                print(
                    f"-> {item.title} | {item.price} {item.currency} | Rating: {item.rating} | URL: {item.url}"
                )

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
