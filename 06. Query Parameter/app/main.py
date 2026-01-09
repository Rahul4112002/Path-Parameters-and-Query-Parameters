from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()

PRODUCTS = [
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": (
            "Your perfect pack for everyday use and walks in the forest. "
            "Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
        ),
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts",
        "price": 22.30,
        "description": (
            "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, "
            "lightweight and soft fabric for breathable and comfortable wear."
        ),
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": (
            "Great outerwear jacket for spring, autumn, and winter, suitable for working, "
            "hiking, camping, and travelling."
        ),
    },
]

@app.get("/products")
def get_products(search : Annotated[str | None, Query(default=None, max_length=5, pattern="^[a-z]+$")] = None):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['title'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS