from fastapi import FastAPI

# 1. Create the "app" instance
app = FastAPI()

# 2. Define a "route"
@app.get("/")
def read_root():
    return {"message": "Hello, I am learning FastAPI!"}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"You are looking at item number {item_id}"}