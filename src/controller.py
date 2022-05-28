from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.db import (
    add_facebook_page,
    delete_facebook_page,
    get_all_facebook_pages,
    get_facebook_page,
    update_facebook_page
)

from src.models.facebook import (
    ErrorResponseModel,
    ResponseModel,
    FacebookPageSchema,
    UpdateFacebookModel
)

router = APIRouter()

app = FastAPI()
app.include_router(router, tags=["Facebook"], prefix="/facebook")


@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World!"}


@app.post("/samir", response_description="Facebook scrapped page data added into the database")
async def add_facebook_page_data(facebook_page: FacebookPageSchema = Body(...)):
    facebook_page = jsonable_encoder(facebook_page)
    new_facebook_page = await add_facebook_page(facebook_page)
    return ResponseModel(new_facebook_page, "Facebook scrapped the database added successfully.")
