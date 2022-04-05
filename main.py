import ao3_api_collection_management.AO3 as AO3
import json
import os

#import py_compile
#py_compile.decompile("./im_menu/crypt.pyc")




# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def load_settings():
    from im_menu import info
    import json
    with open("settings.json", "r") as f:
        settings_dict = json.load(f)
        #defining actual settings:
        info.items_per_page = settings_dict["im_items_per_page"]


#load_settings()

#from im_menu import home_nav

from im_menu import obfuscate

crypt = obfuscate.Obfuscate()
