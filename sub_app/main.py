from fastapi import Depends, FastAPI

from .dependencies import get_token_header, get_query_token

# todo: import routers
from .routers.users import router as user_router
from .routers.items import router as item_router

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(user_router)
app.include_router(item_router)


@app.get("/")
async def root():
    return {"message": "Hello bigger Application"}



