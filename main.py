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


@app.get("/users")
async def list_items():
    return {"message": "list items route"}


@app.get("/users/{user_id}")
async def get_items(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}



