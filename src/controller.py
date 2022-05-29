from fastapi import FastAPI
from src.Scapper.facebook_scrap import Facebook_scrap
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.db import (
    add_facebook_page,
    get_all_facebook_pages,
)

from src.models.facebook import (
    ResponseModel,
)

router = APIRouter()

app = FastAPI()
app.include_router(router, tags=["Facebook"], prefix="/facebook")


@app.post("/scrape/{page_id}")
async def scrape(page_id: str):
    profile = Facebook_scrap(page_id).scrap()
    if "About" not in profile:
        profile["About"] = "None"
    print(type(profile))
    facebook_page = jsonable_encoder(profile)
    new_facebook_page = await add_facebook_page(facebook_page)
    return ResponseModel(new_facebook_page, "Facebook scrapped the database added successfully.")

@app.get("/get/allScrapperPage")
async def scrape():
    new_facebook_page = await get_all_facebook_pages()
    return ResponseModel(new_facebook_page, "Here is all the scrapped facebook page.")


