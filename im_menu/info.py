import re

#logged_in, current_menu, li_msg, session = None

welcome, li_limited, li_locked, collection_id, collection, items_per_page = "", "", "", "", "", ""

logged_in = None
current_menu = None
session = None



#welcome = ""

#li_limited = ""
#li_locked = ""
#li_msg = None

#session = None

#collection_id = ""
#collection = ""

#items_per_page = ""

Yes = re.compile("(Y)|(Yes)", re.IGNORECASE)
No = re.compile("(N)|(No)", re.IGNORECASE)