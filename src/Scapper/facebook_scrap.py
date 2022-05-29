import json

from bson import json_util
from facebook_scraper import get_profile


class Facebook_scrap:

    def __init__(self, page_id):
        self.page_id = page_id

    def scrap(self):
        try:
            profile_json = get_profile(self.page_id)
            return json.loads(json_util.dumps((profile_json)))
        except:
            return {"Error": "page not found"}
