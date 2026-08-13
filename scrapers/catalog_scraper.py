from datetime import datetime, timezone
import re
from typing import List
from urllib.parse import urljoin
from playwright.async_api import Page
from pydantic import ValidationError

from scrapers.base_scraper import BaseScraper
from models.product import ProductSchema


class CatalogScraper(BaseScraper):
    """Scraper implementation for Books to Scrape catalog pages."""

    RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    async def parse(self, page: Page) -> List[ProductSchema]:
        """Parses all product items from the current catalog page."""
        scraped_products: List[ProductSchema] = []

        product_elements = await page.query_selector_all("article.product_pod")
        self.logger.info(
            f"Found {len(product_elements)} product cards on current page."
        )

        for element in product_elements:
            try:
                # 1. Title & URL
                title_anchor = await element.query_selector("h3 a")
                title = (
                    await title_anchor.get_attribute("title") if title_anchor else ""
                )
                relative_url = (
                    await title_anchor.get_attribute("href") if title_anchor else ""
                )
                full_url = urljoin(self.base_url, relative_url)

                # 2. Price
                price_element = await element.query_selector("p.price_color")
                price_text = (
                    await price_element.inner_text() if price_element else "0.0"
                )
                clean_price = float(re.sub(r"[^\d.]", "", price_text))

                # 3. Stock
                stock_element = await element.query_selector("p.instock.availability")
                stock_text = (
                    await stock_element.inner_text() if stock_element else ""
                )
                in_stock = "In stock" in stock_text

                # 4. Rating
                rating_element = await element.query_selector("p.star-rating")
                rating = 1.0
                if rating_element:
                    class_attribute = (
                        await rating_element.get_attribute("class") or ""
                    )
                    for class_name, num_rating in self.RATING_MAP.items():
                        if class_name in class_attribute:
                            rating = float(num_rating)
                            break

                # 5. Populate ProductSchema
                product = ProductSchema(
                    title=title,
                    price=clean_price,
                    currency="GBP",
                    url=full_url,
                    in_stock=in_stock,
                    rating=rating,
                    scraped_at=datetime.now(timezone.utc),
                )
                scraped_products.append(product)

            except ValidationError as ve:
                self.logger.error(f"Pydantic validation error for item: {ve}")
            except Exception as exc:
                self.logger.exception(f"Unexpected error parsing product card: {exc}")

        return scraped_products