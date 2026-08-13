from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class ProductSchema(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the product")
    price: float = Field(..., ge=0, description="Price in USD")
    currency: str = Field(default="USD", max_length=3)
    url: HttpUrl = Field(..., min_length=1, description="Direct URL to product page")
    in_stock: bool = Field(default=True)
    rating: Optional[float] = Field(default=None, ge=0, le=5)
    scraped_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
