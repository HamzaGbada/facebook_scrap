from facebook_scraper import get_profile


class Facebook_scrap:

    def __init__(self, page_id):
        self.page_id = page_id

    def scrap(self):
        try:
            profile_json = get_profile(self.page_id)
            return profile_json
        except:
            print("No page available")
