from fastapi import FastAPI

# 1. Create the "app" instance
app = FastAPI()

# 2. Define a "route"
@app.get("/")
def read_root():
    return {"message": "Hello, I am learning FastAPI!"}