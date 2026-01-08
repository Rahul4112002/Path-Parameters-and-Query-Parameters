from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ProductCategory(Enum):
    books = 'Books'
    electronics = 'Electronics'
    clothing = 'Clothing'
    

@app.get("/products/{category}")
async def single_products(category:ProductCategory):
  return {
    'response': "Single Product",
    'category': category
  }
  
@app.get("/products/{category}")
async def get_product(category:ProductCategory):
  if category == ProductCategory.books:
    return {
      'category': category,
      'message': "Books are awesome"
    }
  elif category == ProductCategory.clothing:
    return {
      'category': category,
      'message': "Cloths are awesome"
    }
  elif category == ProductCategory.electronics:
    return {
      'category': category,
      'message': "Electronics are awesome"
    }
  else:
    return {
      'category': category,
      'message': "Unknown category"
    }