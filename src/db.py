import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://test:test@localhost:27017/test?authSource=admin&retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.facebook_pages

facebook_page_collection = database.get_collection("facebook_page_collection")


def facebook_page_helper(facebook_page) -> dict:
    return {
        "id": str(facebook_page["_id"]),
        "page_name": facebook_page["page_name"],
        "number_follower": facebook_page["number_follower"]
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


# Retrieve a facebook_page with a matching ID
async def get_facebook_page(id: str) -> dict:
    facebook_page = await facebook_page_collection.find_one({"_id": ObjectId(id)})
    if facebook_page:
        return facebook_page_helper(facebook_page)


# Update a facebook_page with a matching ID
async def update_facebook_page(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    facebook_page = await facebook_page_collection.find_one({"_id": ObjectId(id)})
    if facebook_page:
        updated_facebook_page = await facebook_page_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_facebook_page:
            return True
        return False


# Delete a facebook_page from the database
async def delete_facebook_page(id: str):
    facebook_page = await facebook_page_collection.find_one({"_id": ObjectId(id)})
    if facebook_page:
        await facebook_page_collection.delete_one({"_id": ObjectId(id)})
        return True
