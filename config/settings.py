from pydantic import BaseModel

class ScraperSettings(BaseModel):
    base_url: str = "https://books.toscrape.com"
    headless: bool = True
    timeout: int = 30000
    request_delay: float = 1.0

settings = ScraperSettings()
