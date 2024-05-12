from enum import Enum
from typing import Optional
from fastapi import FastAPI, Query

from fastapi import FastAPI
from pydantic import BaseModel

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


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"
    icecream = "ICE CREAM"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }
    return {"food_name": food_name, "message": "i like chocolate milk"}


fake_items_db = [
    {"items_name": "Foo"},
    {"items_name": "Bar"},
    {"items_name": "Baz"}
]


@app.get("/itemsS")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_items(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q": q})
    if not short:
        item.update({
            "description": " Transform writing with efficiency and creativity create, comprehend, refine, and elevate your documents "
        })
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": " Transform writing with efficiency and creativity create, comprehend, refine, and elevate your documents "
            }
        )
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ItemResponse(BaseModel):
    res_name: str
    res_description: str | None = None
    res_price: float
    res_tax: float | None = None
    total_price: float | None = None


@app.post("/items")
async def create_item(item: Item):
    result = ItemResponse(
        res_name=item.name,
        res_description=item.description,
        res_price=item.price,
        res_tax=item.tax,
        total_price=item.price + item.tax
    )
    return result
    # item_dict = item.dict()
    # if item.tax:
    #     item_dict.update(
    #         {"price_with_tax": item.price + item.tax}
    #     )
    # return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {
        "item_id": item_id, **item.dict()
    }
    if q:
        result.update({"q": q})
    return result


@app.get("/itemsp")
async def read_items(p: str | None = Query(None, min_length=3,max_length=10,title="Simple query string",description="This is a sample string")):
    results = {"items": [{"items_id": "Foo"}, {"items_id": "Bar"}]}
    if p:
        results.update({"p": p})
    return results


@app.get("/items_/hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}