import re
import ao3_api_collection_management.AO3 as AO3
from im_menu import info
from im_menu.errors import OutOfRangeError

info.current_menu = "home_nav"
info.logged_in = False

def print_menu():
    if info.logged_in == True:
        info.user = re.sub("(\<User \[)|(\])\>", "", str(info.session.user))
        li_msg = "Log out"
        welcome = f"Welcome, {info.user}."
        li_limited = ""
        li_locked = ""
    elif info.logged_in == False:
        li_msg = "Log in"
        li_limited = " | [Limited]"
        li_locked = " | [Requires Login]"
        welcome = f"Welcome, Guest. Please log in using your AO3 credentials to increase your options."
    
    menu_options = [
        f"{li_msg} (Working)",
        f"Collection Items Manager (Working){li_locked}",
        f"Item List Actor (TBA){li_limited}",
        f"Item List Exporter (TBA){li_limited}",
        "Settings (Working)",
        "End Session (Working)"
    ]
  
    print("\n")
    print(welcome)
    for num, item in enumerate(menu_options, 1):
        print (num, "--", menu_options[num-1] )

def GoToLogin():
    from im_menu import login
#login code for new sessions
    info.current_menu = "login"
    if info.logged_in is False:
        if login.checkSavedLogins() >= 1:
            useSavedLI = login.useSavedLogins()
        else:
            useSavedLI = False
        if useSavedLI is True:
            login.savedLoginsMenu()
        elif login.checkSavedLogins() is None or useSavedLI is False:
            login.manual_login()
    elif info.logged_in is True:
        login.log_out()

def CollectionItemsManager():
    from im_menu import itemManager
    info.current_menu = "collection_item_home"
    itemManager.menu_ItemManager()

def ItemActor():
    print("Handle option \'Item List Actor\'")

def ListMaker():
    print('Handle option \'Item List Exporter\'')

def SettingsMenu():
    from im_menu.settings_menu import settings_menu
    settings_menu()

if info.current_menu == "home_nav":
    while(True):
        print_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
            if option > 6 or option < 1:
                raise OutOfRangeError()
        except(TypeError, OutOfRangeError):
            print("Invalid input. Please enter a number between 1 and 6.")
        #Check what choice was entered and act accordingly
        if option == 1:
            info.current_menu = "login"
            GoToLogin()
        elif option == 2:
            CollectionItemsManager()
        elif option == 3:
            ItemActor()
        elif option == 4:
            ListMaker()
        elif option == 5:
            info.current_menu = "settings"
            SettingsMenu()
        elif option == 6:
            from im_menu.login import log_out
            log_out()
            #technically not necessary as ending the program clears the session where the user is logged in, but just to assuage any extra cautious people a little more
            print("Thank you for using L_GS\'s AO3 Item Manager.")
            exit()