from fastapi import FastAPI

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


# Get all data
@app.get("/product")
async def all_data():
  return PRODUCTS

# Get single data
@app.get("/product/{product_id}")
async def single_data(product_id:int):
  for product in PRODUCTS:
    if product['id'] == product_id:
      return product
    else:
      return {'message': "Product not found"}
    
@app.post("/product/")
async def new_product(new_product:dict):
  PRODUCTS.append(new_product)
  return {'message': "CREATED", 'new_product': new_product}

@app.put("/product/{product_id}")
async def update_data(product_id:int,new_updated_product:dict):
  for index,product in enumerate(PRODUCTS):
    if product['id'] == product_id:
      PRODUCTS[index] = new_updated_product
      return {
        'status': "Product updated",
        'product_id': product_id,
        'updated_product':new_updated_product
      }
  
@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
  for index,product in enumerate(PRODUCTS):
    if product['id'] == product_id:
      PRODUCTS.pop(index)
      return {'message':'DELETED'}