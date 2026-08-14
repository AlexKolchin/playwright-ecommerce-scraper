import json
from pathlib import Path
from typing import List
from models.product import ProductSchema


def save_products_to_json(
    products: List[ProductSchema], file_path: str = "data/products.json"
) -> None:
    """Saves a list of ProductSchema objects into a JSON file."""
    path = Path(file_path)
    # Create data directory if it does not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    # Convert Pydantic models to a list of dictionaries with ISO datetime formatting
    data = [product.model_dump(mode="json") for product in products]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)