from fastapi import FastAPI

from typing import Optional, List  
from pydantic import BaseModel
# 1. Create the "app" instance
app = FastAPI()
my_database = []

# This is your "Template" or Blueprint
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None  # This is optional
    tax: float = 0.0  # This is optional, defaults to 0.0
    is_offer: bool = False  # This is optional, defaults to False
# 2. Define a "route"
@app.get("/")
def read_root():
    return {"message": "Hello, I am learning FastAPI!"}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"You are looking at item number {item_id}"}
@app.get("/users/")
def get_user_info(name: str, age: int):
    return {
        "message": f"Hello {name}!",
        "age_next_year": age + 1
    }
@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + item.tax
    my_database.append(item)
    return {
        "message": f"Item '{item.name}' created successfully!",
        "item_details": item,
        "total_with_tax": total_price,
        # "message": f"Item '{item.name}' created successfully!",
       "current_db_size": len(my_database)
    }

@app.get("/all-items/")
def get_all_items():
    return {"all_items": my_database}