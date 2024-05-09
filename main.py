from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post root"}


@app.put("/")
async def put():
    return {"message": "hello from the put root"}


@app.get("/items")
async def list_items():
    return {"message": "list items route"}


@app.get("/items/{item_id}")
async def get_user(item_id: int):
    return {"item_id": item_id}


@app.get("/items/me")
async def get_current_user():
    return {"message": "This is the current user"}
