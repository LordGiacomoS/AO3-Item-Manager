import os
import re
import ao3_api_collection_management.AO3 as AO3
from Menu import info, login

info.current_menu = "home_nav"

Yes = re.compile("(Y)|(Yes)", re.IGNORECASE)
No = re.compile("(N)|(No)", re.IGNORECASE)

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
    
    menu_options = [li_msg, f"Collection Items Manager (WIP){li_locked}", f"Item List Actor (TBA){li_limited}", f"Item List Exporter (TBA){li_limited}", "End Process (Automatically logs out user)"]
    print("\n")
    print(welcome)
    for num, item in enumerate(menu_options, 1):
        print (num, "--", menu_options[num-1] )

def GoToLogin():
#login code for new sessions
    info.current_menu = "login"
    if info.logged_in is False:
        if login.checkSavedLogins() is not None:
            useSavedLI = login.useSavedLogins()
        if useSavedLI is True:
            login.savedLoginsMenu()
        elif login.checkSavedLogins() is None or useSavedLI is False:
            login.manual_login()
    elif info.logged_in is True:
        login.log_out()

def CollectionItemsManager():
    info.current_menu = "collection_item_manager"
    print("Handle option \'Collection Items Manager\'")

def ItemActor():
    print("Handle option \'Item List Actor\'")

def ListMaker():
    print('Handle option \'Item List Exporter\'')


if info.current_menu == "home_nav":
    while(True):
        print_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Invalid input. Please enter a number between 1 and 5.")
        #Check what choice was entered and act accordingly
        if option == 1:
            GoToLogin()
        elif option == 2:
            CollectionItemsManager()
        elif option == 3:
            ItemActor()
        elif option == 4:
            ListMaker()
        elif option == 5:
            login.log_out()
            #technically not necessary as it logs user out automatically because program ends, but just to 
            print("Thank you for using L_GS\'s AO3 Item Manager.")
            exit()
        else:
            print("Invalid input.")