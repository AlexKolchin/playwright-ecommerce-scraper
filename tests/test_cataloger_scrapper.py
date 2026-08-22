import pytest
from playwright.async_api import async_playwright
from scrapers.catalog_scraper import CatalogScraper


@pytest.mark.asyncio
async def test_parse_catalog_page(sample_catalog_html: str):
    """Tests parsing logic using mocked HTML content."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Intercept network requests and return fake HTML
        await page.route(
            "https://books.toscrape.com/",
            lambda route: route.fulfill(
                status=200,
                content_type="text/html",
                body=sample_catalog_html,
            ),
        )

        await page.goto("https://books.toscrape.com/")

        scraper = CatalogScraper(base_url="https://books.toscrape.com/")
        products = await scraper.parse(page)

        # Assertions
        assert len(products) == 2

        # Check first item details
        assert products[0].title == "A Light in the Attic"
        assert products[0].price == 51.77
        assert products[0].in_stock is True
        assert products[0].rating == 3.0

        # Check second item details
        assert products[1].title == "Tipping the Velvet"
        assert products[1].price == 53.74
        assert products[1].in_stock is False
        assert products[1].rating == 1.0

        await browser.close()


@pytest.mark.asyncio
async def test_scrape_all_pages_pagination(sample_catalog_html: str):
    """Tests that pagination correctly stops when max_pages limit is reached."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Intercept all catalog URLs
        await page.route(
            "**/books.toscrape.com/**",
            lambda route: route.fulfill(
                status=200,
                content_type="text/html",
                body=sample_catalog_html,
            ),
        )

        scraper = CatalogScraper(base_url="https://books.toscrape.com/")

        products = await scraper.scrape_all_pages(
            page, "https://books.toscrape.com/", max_pages=1
        )

        assert len(products) == 2

        await browser.close()
