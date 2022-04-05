#import ao3_api_collection_management.AO3 as AO3
#import os

def load_settings():
    from im_menu import info
    import json
    with open("settings.json", "r") as f:
        settings_dict = json.load(f)
        #defining actual settings:
        info.items_per_page = settings_dict["im_items_per_page"]

load_settings()

from im_menu import home_nav