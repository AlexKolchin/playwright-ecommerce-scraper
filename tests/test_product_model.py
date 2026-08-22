from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from models.product import ProductSchema


def test_product_schema_valid_creation():
    """Tests that a valid ProductSchema object is instantiated correctly."""
    product = ProductSchema(
        title="Test Book",
        price=19.99,
        currency="GBP",
        url="https://books.toscrape.com/test.html",
        in_stock=True,
        rating=4.5,
        scraped_at=datetime.now(timezone.utc),
    )
    assert product.title == "Test Book"
    assert product.price == 19.99
    assert product.currency == "GBP"
    assert product.rating == 4.5


def test_product_schema_invalid_price():
    """Tests that ProductSchema raises ValidationError on negative price."""
    with pytest.raises(ValidationError):
        ProductSchema(
            title="Invalid Price Book",
            price=-5.00, # Price must be >= 0
            currency="GBP",
            url="https://books.toscrape.com/test.html",
            in_stock=True,
            rating=4.0,
            scraped_at=datetime.now(timezone.utc),
        )


def test_product_schema_invalid_rating():
    """Tests that ProductSchema raises ValidationError on rating out of range."""
    with pytest.raises(ValidationError):
        ProductSchema(
            title="Invalid Rating Book",
            price=10.00,
            currency="GBP",
            url="https://books.toscrape.com/test.html",
            in_stock=True,
            rating=6.0, # Rating must be <= 5.0
            scraped_at=datetime.now(timezone.utc),
        )
