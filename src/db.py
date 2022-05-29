import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://test:test@localhost:27017/test?authSource=admin&retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.facebook_pages

facebook_page_collection = database.get_collection("facebook_page_collection")


def facebook_page_helper(facebook_page) -> dict:
    return {
        "id": str(facebook_page["_id"]),
        "Name": facebook_page["Name"],
        "About": facebook_page["About"]
    }


# Retrieve all facebook_pages present in the database
async def get_all_facebook_pages():
    facebook_pages = []
    async for facebook_page in facebook_page_collection.find():
        facebook_pages.append(facebook_page_helper(facebook_page))
    return facebook_pages


# Add a new facebook_page into to the database
async def add_facebook_page(facebook_page_data: dict) -> dict:
    facebook_page = await facebook_page_collection.insert_one(facebook_page_data)
    new_facebook_page = await facebook_page_collection.find_one({"_id": facebook_page.inserted_id})
    return facebook_page_helper(new_facebook_page)

