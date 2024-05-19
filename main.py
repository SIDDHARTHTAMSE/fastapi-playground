
# Activate python in powershell:  .\env\Scripts\Activate.ps1'

from datetime import datetime, time, timedelta
from enum import Enum
from typing import Optional, Literal, Union
from fastapi import (
    Body,
    Depends,
    FastAPI,
    Query,
    Path,
    Cookie,
    Header,
    status,
    Form,
    File,
    UploadFile,
    HTTPException,
    Request,
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.responses import JSONResponse, PlainTextResponse
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import HTMLResponse

app = FastAPI()


#
# @app.get("/")
# async def root():
#     return {"message": "hello world"}
#
#
# @app.post("/")
# async def post():
#     return {"message": "hello from the post root"}
#
#
# @app.put("/")
# async def put():
#     return {"message": "hello from the put root"}
#
#
# @app.get("/users")
# async def list_items():
#     return {"message": "list items route"}
#
#
# @app.get("/users/{user_id}")
# async def get_items(user_id: str):
#     return {"user_id": user_id}
#
#
# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "this is the current user"}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#     icecream = "ICE CREAM"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
#
#     if food_name.value == "fruits":
#         return {
#             "food_name": food_name,
#             "message": "you are still healthy, but like sweet things",
#         }
#     return {"food_name": food_name, "message": "i like chocolate milk"}
#
#
# fake_items_db = [
#     {"items_name": "Foo"},
#     {"items_name": "Bar"},
#     {"items_name": "Baz"}
# ]
#
#
# @app.get("/itemsS")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_items(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({
#             "description": " Transform writing with efficiency and creativity create, comprehend, refine, and elevate your documents "
#         })
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(
#         user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": " Transform writing with efficiency and creativity create, comprehend, refine, and elevate your documents "
#             }
#         )
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class ItemResponse(BaseModel):
#     res_name: str
#     res_description: str | None = None
#     res_price: float
#     res_tax: float | None = None
#     total_price: float | None = None
#
#
# @app.post("/items")
# async def create_item(item: Item):
#     result = ItemResponse(
#         res_name=item.name,
#         res_description=item.description,
#         res_price=item.price,
#         res_tax=item.tax,
#         total_price=item.price + item.tax
#     )
#     return result
#     # item_dict = item.dict()
#     # if item.tax:
#     #     item_dict.update(
#     #         {"price_with_tax": item.price + item.tax}
#     #     )
#     # return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {
#         "item_id": item_id, **item.dict()
#     }
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/itemsp")
# async def read_items(p: str | None = Query(None, min_length=3,max_length=10,title="Simple query string",description="This is a sample string")):
#     results = {"items": [{"items_id": "Foo"}, {"items_id": "Bar"}]}
#     if p:
#         results.update({"p": p})
#     return results
#
#
# @app.get("/items_/hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}
#
#
# @app.get("/items_validation/{item_id}")
# async def read_item_validation(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", get=10, le=100),
#         q: str = "hello",
#         size: float = Query(..., gt=0, lt=7.75)
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q": q})
#     return results

# Part 7 --> Body - Multiple Parameters

#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: str
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")  # /items/{item_id} --> API path
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
#         q: str | None = None,
#         item: Item | None = None,
#         user: User,
#         importance: int = Body(...)
# ):
#         results = {"item_id": item_id}
#         if q:
#             results.update({"q": q})
#         if item:
#             results.update({"item": item})
#         if user:
#              results.update({"user": user})
#         if importance:
#             results.update({"importance": importance})
#         return results
#
# @app.put("/items-x/{item_id}")  # /items/{item_id} --> API path
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
#         q: str = Query(),
#         item_name: str = Query(),
#         item_description: str = Query(),
#         item_price: int = Query(),
#         item_tax: int = Query(),
#         user_name: str = Query(),
#         full_name: str = Query(),
#         user: User,
#         importance: int = Body(...)
# ):
#

#
# class Item(BaseModel):
#     name: str | None = Field(
#         ...,
#         description="Name of the electronic item"
#     )
#     description: str | None = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The prize must be greater than zero")
#     tax: float | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

#
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: list[Image] | None = None
#
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]
#
#
# @app.put("/items/{items_id}")
# async def update_item(item_id: int, item:Item):
#     results = {"items_id": item_id, "item": item}
#     return results
#
#
# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
#
# @app.post("/image/multiple")
# async def create_multiple_images(image: list[Image]):
#     return image
#
#
# @app.post("/blah")
# async def create_blah(blahs: dict[int, float]):
#     return blahs

#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: str
#     tax: float | None = None
#
#     class Config:
#         schema_extra = {
#            "example": {
#                "name": "Foo",
#                "description": "A very nice Item",
#                "price": 16.25,
#                "tax": 1.67,
#            }
#         }
#
#
# class Product(BaseModel):
#     a: int
#     class Config:
#         schema_extra = {
#             "examples": [
#                 {
#                     "a": 100
#                 },
#                 {"a": 200}
#             ]
#         }
# @app.put("/items2/{item_id}")
# async def update_item2(
#         item: Product
# ):
#     print(item)
#     return "Hi"
#
# Declare Request Example data


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         ...,
#         example={
#             "normal": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 16.25,
#                 "tax": 1.67,
#             },
#             "converted": {
#                 "summary": "An example with converted data",
#                 "description": "FastAPI can converted price `string` to actual `numbers` automatically",
#                 "value": {"name": "Bar", "price": "16.25"},
#
#             },
#             "Invalid": {
#                 "summary": "Invalid data is rejected with an error",
#                 "value": {"name": "Baz", "price": "sixteen point two five"}
#             }
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# Extra Data Types


# @app.put("/item/{item_id}")
# async def read_items(
#         item_id: UUID,
#         start_date: datetime | None = Body(None),
#         end_date: datetime | None = Body(None),
#         repeat_at: time | None = Body(None),
#         process_after: timedelta | None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date,
#         "end_date": end_date,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

# Cookie and Header Parameter


# @app.get("/items")
# async def read_items(
#         cookie_id: str | None = Cookie(None),
#         accept_encoding: str | None = Header(None),
#         sec_ch_ua: str | None = Header(None),
#         user_agent: str | None = Header(None),
#         x_token: list[str] = Header([])
# ):
#
#     return {
#         "cookie_id": cookie_id,
#         "accept_encoding": accept_encoding,
#         "sec_ch_ua": sec_ch_ua,
#         "user_agent": user_agent,
#         "x_token": x_token
#     }

# Response Model
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }
#
#
# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]
#
#
# @app.post("/items/", response_model=Item)
# async def create_item(item_id: Item):
#     return item_id
#
#
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user
#
#
# @app.get(
#     "/item,{item_id}/name",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(
#         item_id: Literal["foo", "bar", "baz"]
# ):
#     return items[item_id]
#
#
# @app.get(
#     "/item,{item_id},public",
#     response_model=Item,
#     response_model_exclude={"tax"},
# )
# async def read_items_public_data(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]

# Extra Models

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
#
# class UserInDB(BaseModel):
#     hashed_password: str
#
#
# def fake_password_hasher(raw_password: str):
#     return f"supersecret{raw_password}"
#
#
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(raw_password=user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User 'saved'.")
#     return user_in_db
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved
#
#
# class BaseItem(BaseModel):
#     description: str
#     type: str
#
#
# class CarItem(BaseItem):
#     type: str = "car"
#
#
# class PlaneItem(BaseItem):
#     type: str = "plane"
#     size: int
#
#
# items = {
#     "item1": {
#         "description": "All my friends driver a low rider",
#         "type": "car"
#     },
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }
#
#
# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]
#
#
# class ListItem(BaseModel):
#     name: str
#     description: str
#
#
# list_items = [
#     {"item1": "foo", "description": "There comes my hero"},
#     {"item2": "Red", "description": "It's my aeroplane"},
# ]
#
#
# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#     return items

# Response Status Codes

# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}
#
#
# @app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#     print("pk", pk)
#     return pk
#
#
# @app.get("/items", status_code=status.HTTP_302_FOUND)
# async def read_items_redirect():
#     return {"hello": "world"}

# Form Fields

# @app.post("/login/")
# async def login(username: str = Form(...), password: str = Body(...)):
#     print("username", password)
#     return {"username": username}
#
#
# @app.post("/login-json/")
# async def login_json(username: str = Body(...), password: str = Body(...)):
#     print("username", password)
#     return {"username": username}


# Request Files

# @app.post("/files/")
# async def create_file(
#         files: list[bytes] = File(..., description="A file read as bytes")
# ):
#     return {"file_sizes": [len(file) for file in files]}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(
#         files: list[UploadFile] = File(..., description="A file read as UploadFile")
# ):
#     return {"filename": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
#     Response Model
# # class Item(BaseModel):
# #     name: str
# #     description: str | None = None
# #     price: float
# #     tax: float | None = None
# #     tags: list[str] = []
#     """
#     return HTMLResponse(content=content)


# Request Forms and Files
# @app.post("/files/")
# async def create_file(
#         file: bytes = File(...),
#         fileb: UploadFile = File(...),
#         token: str = Form(...)
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#     }

# Handling Errors

# items = {"foo": "The Foo Wrestlers"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Item not found",
#             headers={"x-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}
#
#
# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
#
#
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow"},
#     )
#
#
# @app.get("/unicorns/{name}")
# async def read_unicorns(name: str):
#     if name == 'yolo':
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_items(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)
#
#
# @app.get("/validation_items{item_id}")
# async def read_validation_items(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! i dont like 3.")
#     return {"item_id": item_id}


# @app.exception_handler(RequestValidationError)
# async def validation_exceptional_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )
#
#
# class Item(BaseModel):
#     title: str
#     size: int
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item
#
#
# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)
#
#
# @app.exception_handler(RequestValidationError)
# async def validation_exceptional_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)
#
#
# @app.get("/blah_items/{item_id}")
# async def read_items(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I dont like 3.")
#     return {"item_id": item_id}


# Path Operation Configuration

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float
#     tag: set[str] = set()
#
#
# class Tags(Enum):
#     items = "Items"
#     users = "Users"
#
#
# @app.post(
#     "/items/",
#     response_model=Item,
#     status_code=status.HTTP_201_CREATED,
#     tags=[Tags.items],
#     summary="Create an Item-type item",
#     # description="Create an item with all the information: "
#     #             "name; description; price; and a set of "
#     #             "unique tags",
#     response_description="The created item"
# )
# async def create_item(item: Item):
#     """
#     Create an item with all the information:
#
#
#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can amit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item
#
#
# @app.get("/items", tags=[Tags.items])
# async def read_items():
#     return [{"items": "Foo", "price": 42}]
#
#
# @app.get("/users/", tags=[Tags.users])
# async def read_users():
#     return [{"username": "PhoebeBuffay"}]
#
#
# @app.get("/element/", tags=[Tags.items], deprecated=True)
# async def read_element():
#     return [{"item_id": "Foo"}]

# JSON Compatible Encoder

# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.5
#     tags: list[str] = []
#
#
# items = {
#     "foo": {
#         "name": "Foo",
#         "price": 50.2
#     },
#     "bar": {
#         "name": "Bar",
#         "description": "The bartenders",
#         "price": 62,
#         "tax": 20.2
#     },
#     "baz": {
#         "name": "Baz",
#         "description": None,
#         "price": 50.2,
#         "tax": 10.5,
#         "tags": []
#     },
# }
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items.get(item_id)
#
#
# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded
#
#
# @app.patch("/items/{item_id}", response_model=Item)
# def patch_item(item_id: str, item: Item):
#     stored_item_data = items.get(item_id)
#     if stored_item_data is not None:
#         stored_item_model = Item(**stored_item_data)
#     else:
#         stored_item_model = Item()
#     update_data = item.dict()
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     print(items)
#     return updated_item


# Dependencies Intro

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}
#
#
# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons
#
#
# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons

# Classes as Dependencies

# fake_items_db = [
#     {"item_name": "Foo"},
#     {"Item_name": "Bar"},
#     {"item_name": "Baz"}
# ]
#
#
# class CommonQueryParams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit
#
#
# @app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip + commons.limit]
#     response.update({"items": items})
#     return response

# Sub-Dependencies
def query_extractor(q: str | None = None):
    return q


def query_or_body_extractor(
        q: str = Depends(query_extractor), last_query: str | None = Body(None)
):
    if not q:
        return last_query
    return q


@app.post("/item")
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {"q_or_body": query_or_body}
