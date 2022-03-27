import re

logged_in = False
current_menu = None

welcome = ""

li_limited = ""
li_locked = ""
li_msg = None

session = None


Yes = re.compile("(Y)|(Yes)", re.IGNORECASE)
No = re.compile("(N)|(No)", re.IGNORECASE)