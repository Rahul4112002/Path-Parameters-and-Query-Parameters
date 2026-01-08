from fastapi import FastAPI

app = FastAPI()

@app.get('/products/static')
async def single_products_static():
  return {
    'response': "Single Product",
  }

@app.get("/products/{product_id}")
async def single_products(product_id:str):
  return {
    'response': "Single Product",
    'product id': product_id
  }