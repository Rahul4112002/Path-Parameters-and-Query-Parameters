from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(limit: int,category: str | None = None):
    return {"category": category,"limit": limit}