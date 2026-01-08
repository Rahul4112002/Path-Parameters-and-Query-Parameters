from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
async def all_products():
  return {
    'response': "All Products"
  }
  
@app.get("/products/{product_id}")
async def single_products(product_id):
  return {
    'response': "Single Product",
    'product id': product_id
  }
  
@app.post("/products")
async def create_product(new_product: dict):
  return {
    'response': "Product created" ,
    'product': new_product
  }
  
@app.put("/products/{product_id}")
async def update_product(new_update_product: dict,product_id:int):
  return {
    'response': "Product Data Updated" ,
    'product': new_update_product,
    'product_id': product_id
  }
  
@app.patch("/products/{product_id}")
async def partial_update_product(new_update_product: dict,product_id:int):
  return {
    'response': "Partial Data Updated" ,
    'product': new_update_product,
    'product_id': product_id
  }
  
@app.delete("/products/{product_id}")
async def delete_product(product_id):
  return {
    'response': "Product Delete",
    'product id': product_id
  }