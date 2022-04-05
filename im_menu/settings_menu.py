from im_menu import info
import json

from im_menu.errors import OutOfRangeError

def save_ipp(ipp):
    with open("settings.json", "r") as f:
        settings_dict = json.load(f)
        if type(ipp) == int:
            settings_dict["im_items_per_page"] = ipp
        obj = json.dumps(settings_dict, indent=2)
    with open("settings.json", "w") as f:
        f.write(obj)


def del_profile():
    with open("logins.json") as f:
        logins_dict = json.load(f)
    
    log_dict_len = len(logins_dict["logins"])
    print("\n")
    users = []
    option = ""
    for login in logins_dict["logins"]:
        users.append(login["id"]) 
        #log_num = login["num"]
            
    for num, login in enumerate(users, 1):
        print(f'{num} -- "{login}"')

    exit_num = log_dict_len+1
    print(f"{exit_num} -- Cancel")
  
    while (option==""):
        try:
            option = int(input("Enter your choice: "))
        
            if option == exit_num:
                info.current_menu = "settings"
                return
            elif 1 <= option < exit_num:
            #* Deletes the login profile
                new = list(filter(lambda i: i["num"] != option, logins_dict["logins"]))

            #* Corrects the numbers
                count = 0
                for login in new:
                    count += 1
                    if login["num"] > count:
                        login["num"] = count
                      
            #* Updates the json file    
                logins_dict["logins"] = new
                obj = json.dumps(logins_dict, indent=2)
                with open("logins.json", "w") as f:
                    f.write(obj)
            #* Going back to last menu
                info.current_menu = "settings"
                return
            elif option > exit_num or option < 1:
                raise OutOfRangeError("Number out of range")
        except (TypeError, OutOfRangeError):
            print(f"Invalid input. Please enter a number from 1 to {exit_num}.")
            option = ""

def settings_menu():
    info.current_menu = "settings"
    action = ""
    from im_menu.login import checkSavedLogins
    saved_logins = checkSavedLogins()
    if saved_logins <= 0:
        sl_msg = "Delete Saved Login Profile(s) [None to Delete]"
    elif saved_logins >= 1:
        sl_msg = f"Delete Saved Login Profile(s) [Profiles: {saved_logins}]"
 
    menu_options = [
        f"Set Item Manager items per page [Currently: {info.items_per_page}]",
        sl_msg,
        "Return to Main Menu"
    ]

    while(info.current_menu=="settings"):
        print("\n")
        for num, item in enumerate(menu_options, 1):
            print (num, "--", menu_options[num-1] )

        try:
            action = int(input("Enter your choice: "))
            if action > 3 or action < 1:
                raise OutOfRangeError()
            elif action == 1:
                ipp_input = ""
                while(ipp_input == ""):
                    try:
                        ipp_input = int(input(f"Set number of items per page [Currently: {info.items_per_page}]: "))
                        info.items_per_page = ipp_input
                        if ipp_input < 1 or ipp_input > 100:
                            raise OutOfRangeError()
                    except(TypeError, OutOfRangeError):
                        print(f"Invalid input. Please enter a number from 1 to 100.")
        
                save_ipp(info.items_per_page)
                settings_menu()
            elif action == 2:
                info.current_menu = "profile_deleter"
                del_profile()
            elif action == 3:
                info.current_menu = "home_nav"
                return
        except (TypeError, OutOfRangeError):
            print("Invalid input. Please enter a number between 1 and 3.")
