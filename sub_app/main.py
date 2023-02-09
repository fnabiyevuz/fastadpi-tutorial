from fastapi import Depends, FastAPI

from .dependencies import get_query_token
from .routers import users, items

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users)  # users router
app.include_router(items)  # items router


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
