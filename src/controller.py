from fastapi import FastAPI
from src.Scapper.facebook_scrap import Facebook_scrap
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.db import (
    add_facebook_page,
    insert_page,
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

@app.get("/scrape/{page_id}")
async def scrape(page_id: str):
    profile = Facebook_scrap(page_id).scrap()
    return profile

@app.post("/scir/{page_id}")
async def scrape(page_id: str):

    profile = Facebook_scrap(page_id).scrap()
    # facebook_page = jsonable_encoder(profile)
    # profile = {
    #             "page_name": "Cr7",
    #             "number_follower": 100
    #         }
    print(type(profile))
    facebook_page = jsonable_encoder(profile)
    new_facebook_page = await add_facebook_page(facebook_page)
    return ResponseModel(new_facebook_page, "Facebook scrapped the database added successfully.")
    return type(profile)



@app.post("/samir", response_description="Facebook scrapped page data added into the database")
async def add_facebook_page_data(facebook_page: FacebookPageSchema = Body(...)):
    print(type(facebook_page))
    facebook_page = jsonable_encoder(facebook_page)
    print("BBBBBBBBBBBBBBBBBBBBBBBBBBbbbb")
    print(type(facebook_page))
    new_facebook_page = await add_facebook_page(facebook_page)
    return ResponseModel(new_facebook_page, "Facebook scrapped the database added successfully.")
