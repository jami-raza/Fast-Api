from fastapi import FastAPI

app = FastAPI()

# Get endpoint
@app.get("/")
async def get():
    return {"message": "Hello World"}

# Get path parameters endpoint
@app.get("/items/{item_id}")
async def getPath(item_id:int):
    print("Get path parameters endpoint")
    return {"message": item_id}

# Get query parameters endpoint
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def getQuery(skip: int = 0, limit: int = 10):
    print("Get path parameters endpoint")
    return fake_items_db[skip : skip + limit]