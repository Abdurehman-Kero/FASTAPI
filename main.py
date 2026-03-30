from fastapi import FastAPI
from pydantic import BaseModel
# 1. Create the "app" instance
app = FastAPI()

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
# This is your "Template" or Blueprint
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False  # This is optional, defaults to False
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": f"Item '{item.name}' created successfully!",
        "item_details": item
    }