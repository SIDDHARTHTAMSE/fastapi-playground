
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
    BackgroundTasks
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles

from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from passlib.context import CryptContext
from jose import jwt, JWTError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
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

# def query_extractor(q: str | None = None):
#     return q
#
#
# def query_or_body_extractor(
#         q: str = Depends(query_extractor), last_query: str | None = Body(None)
# ):
#     if not q:
#         return last_query
#     return q
#
#
# @app.post("/item")
# async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
#     return {"q_or_body": query_or_body}

# Dependencies in path operation decorators

# async def verify_token(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")
#
#
# async def verify_key(x_key: str = Header(...)):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#
#
# @app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "bar"}]

# Security, First Steps

# auth2_schema = OAuth2PasswordBearer(tokenUrl="token")
#
# fake_users_db={
#     "johndeo": dict(
#         username="johndeo",
#         full_name="John Deo",
#         email="Johndeo@example.com",
#         hashed_password="fakehashedsecret",
#         disable=False
#     ),
#     "alice": dict(
#         username="alice",
#         full_name="Alice Wondersone",
#         email="alice@example.com",
#         hashed_password="fakehashedsecret2",
#         disable=True
#     )
# }
#
#
# def fake_hash_password(password: str):
#     return f"fakehashed{password}"
#
#
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disable: bool | None = None
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# def fake_decode_token(token):
#     return get_user(fake_users_db, token)
#
#
# async def get_current_user(token: str = Depends(auth2_schema)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disable:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     print(user_dict)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     print(form_data.password, hashed_password, user.hashed_password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
#
#
# @app.get("/users/me")
# async def get_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# @app.get("/items")
# async def read_items(token: str = Depends(auth2_schema)):
#     return {"token": token}


# Security, OAuth2 Bearer and JWT
# SECRET_KEY = "thequickbrownfoxjumpsoverthelazydog"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
# fake_users_db = dict(
#     johndoe=dict(
#         username="johndoe",
#         full_name="John Doe",
#         email="johndoe@example.com",
#         hashed_password="$2b$12$f32NX5t.zKCJO6DAJJPxQ.8pT4XaD/t8/LBx/pXP7nCFr49zjM/Nu",
#         disable=False
#     )
# )
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: str | None = None
#
#
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disable: bool = False
#
#
# class UserId(User):
#     hashed_password: str
#
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
#
#
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)
#
#
# def get_password_hash(password):
#     return pwd_context.hash(password)
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserId(**user_dict)
#
#
# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
#
#
# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
#
# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# async def get_current_user(token: str = Depends(oauth2_schema)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"}
#     )
#
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive User")
#     return current_user
#
#
# @app.get("/users/me", response_model=User)
# async def get_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# @app.get("/users/me/items")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]
#
# # Middleware and CORS
# class MyMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         start_time = datetime.now()
#         response = await call_next(request)
#         process_time = (datetime.now() - start_time).total_seconds()
#         response.headers['X-process-Time'] = str(process_time)
#         return response
#
#
# origins = ["https://localhost:8000", "https://localhost:3000"]
# app.add_middleware(MyMiddleware)
# app.add_middleware(CORSMiddleware, allow_origins=origins)
#
#
# @app.get("/blah")
# async def blah():
#     return {"hello": "world"}

# Background Tasks
# import time
#
#
# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         time.sleep(5)
#         email_file.write(content)
#
#
# @app.get("/send-notification/{email}", status_code=202)
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}
#
#
# def write_log(message: str):
#     with open('log.txt', mode='a') as log:
#         log.write(message)
#
#
# def get_query(background_tasks: BackgroundTasks, q: str | None = None):
#     if q:
#         message = f"found query: {q}\n"
#         background_tasks.add_task(write_log, message)
#     return q
#
#
# @app.post("/send-notification/{email}")
# async def send_notification(
#         email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
# ):
#     message = f"message to {email}\n"
#     background_tasks.add_task(write_log, message)
#     return {"message": "Message sent", "query": q}


# Metadata and Docs URLs

# description = """
# ChimichangeApp API helps you do awesome stuff.
#
# ## Items
#
# You can **read items**.
#
# # Users
#
# You will able to:
#  * **Create users** (_not implemented_).
#  * **Read users** (_not implemented_).
#
# """
#
# tags_metadata = [
#     dict(
#         name="users",
#         description="Operation with users. The **login** logic is also here.",
#     ),
#     dict(
#         name="items",
#         description="Manage items. So _fancy_ they have their own docs.",
#         externalDocs=dict(
#             description="Items external docs",
#             url="http://www.jvp.design"
#         ),
#     ),
# ]
#
#
# app = FastAPI(
#     title="ChemichangeApp",
#     description=description,
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact=dict(
#         name="Deadpoolio the Amazing",
#         url="http://x-force.example.com/contact",
#         email="dp@x-force.example.com",
#     ),
#     license_info=dict(
#         name="Apache 2.0",
#         url="https://www.apache.org/licenses/LICENSE-2.0.HTML",
#     ),
#     openapi_tags=tags_metadata,
#     openapi_url="/api/v1/openapi.json",
#     docs_url="/hello-world",
#     redoc_url=None,
# )
#
#
# @app.get("/users", tags=["users"])
# async def get_users():
#     return [dict(name="Harry", dict="Rony")]
#
#
# @app.get("/items", tags=["items"])
# async def read_items():
#     return [dict(name="wand"), dict(name="flying broom")]


## Static Files, Testig and Debugging

# app.mount("/static", StaticFiles(directory="static"), name="static")

fake_secret_token = "coneofsilence"
fake_db = dict(
    foo=dict(
        id="foo",
        title="Foo",
        description="There goes my hero",
    ),
    bar=dict(
        id="bar",
        title="Bar",
        description="The bartenders",
    )
)


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid x-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid x-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=408, detail="Item already exist")
    fake_db[item.id] = item
    return item
