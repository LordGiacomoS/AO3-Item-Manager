import re, json
import ao3_api_collection_management.AO3 as AO3
from pwinput import pwinput

from im_menu import info, crypt
from im_menu.errors import OutOfRangeError, UnrecognizedResponseError


callsign = ""
passkey = ""

crypt = crypt.Crypt()

with open("logins.json") as f:
    logins_dict = json.load(f)

log_dict_len = len(logins_dict["logins"])

#basic log out actions
def log_out():
    if info.session is not None:
        info.session.logout()
    info.logged_in = False
    info.current_menu = "home_nav"

#Basic login screen
def manual_login():
    print("\n")
    callsign = ""
    passkey = ""
    
    save_login = ""
    id = ""

    while(callsign == ""):
        try:
            callsign = str(input("Enter your username or email address: "))
        except(TypeError):
            print("Invalid input.")
            return
          
    while(passkey == ""):
        try:
            passkey = pwinput(prompt="Enter your password: ")
        except:
            print("Invalid input.")
            return
          
    if passkey is not None and callsign is not None:
        try:
            info.session = AO3.Session(callsign, passkey)
        except AO3.utils.LoginError as LoginError:
            print(repr(LoginError))
            info.current_menu = "home_nav"
            return

    while(save_login == ""):
        try:
            info.user = re.sub("(\<User \[)|(\])\>", "", str(info.session.user))
            print("\n")
            print(f"Login successful. Welcome, {info.user}.")
            print("\n")
            s_l_string = str(input("Would you like to save this profile for future sessions? (Warning, this feature is currently extremely insecure) Y/N: "))
            if re.search(info.Yes, s_l_string) is not None:
                save_login = True
            elif re.search(info.No, s_l_string) is not None:
                save_login = False
            else:
                raise UnrecognizedResponseError() 
        except(TypeError, UnrecognizedResponseError):
            print("Invalid Input. Please enter \"Yes\" or \"No\".")

    if save_login == True:
        while(id == ""):
            try:
                id = str(input("Enter name for profile: "))
            except(TypeError):
                print("Invalid input.")
                return
                
    if passkey is not None and callsign is not None and save_login is not None:
        if save_login == True:
            user = crypt.encrypt(callsign)
            key = crypt.encrypt(passkey)
            logins_dict["logins"].append({"num": log_dict_len+1, "id": id, "user": user, "password": key})
            obj = json.dumps(logins_dict, indent=2)
            with open("logins.json", "w") as f:
                f.write(obj)
        info.logged_in = True
    info.current_menu = "home_nav"
  
def checkSavedLogins():
    return log_dict_len

def useSavedLogins():
    if log_dict_len is not None:
        use_saved_login = ""
        while(use_saved_login == "" and log_dict_len == 1):
            try:
                if log_dict_len == 1:    
                    usl_string = str(input("Saved login available. Would you like to use it? Y/N: "))
                if re.search(info.Yes, usl_string) is not None:
                    use_saved_login = True
                elif re.search(info.No, usl_string) is not None:
                    use_saved_login = False
                else:
                    raise UnrecognizedResponseError()
            except(TypeError, UnrecognizedResponseError):
                print("Invalid Input. Please enter \"Yes\" or \"No\".")

        while(use_saved_login == "" and log_dict_len > 1):
            try:
                if log_dict_len > 1:    
                    usl_string = str(input("Saved logins available. Would you like to use one? Y/N: "))
                if re.search(info.Yes, usl_string) is not None:
                    use_saved_login = True
                elif re.search(info.No, usl_string) is not None:
                    use_saved_login = False    
                else:
                    raise UnrecognizedResponseError()
            except(TypeError, UnrecognizedResponseError):      
                print("Invalid Input. Please enter \"Yes\" or \"No\".")
    return use_saved_login

def savedLoginsMenu():
    if log_dict_len == 1:
        for login in logins_dict["logins"]:
            user = login["user"]
            key = login["password"]
            callsign = crypt.decrypt(string=user)
            passkey = crypt.decrypt(string=key)
            info.session = AO3.Session(callsign, passkey)
            info.logged_in = True
              
    if log_dict_len > 1:
        users = []
        for login in logins_dict["logins"]:
            users.append(login["id"]) 
            
        for num, login in enumerate(users, 1):
            print(num, "--", login)

        while info.logged_in == False:
            try:
                login_num = int(input("Enter your choice: "))
                if login_num > log_dict_len or login_num < 1:
                    raise OutOfRangeError()
            except(TypeError, OutOfRangeError):
                print(f"Wrong input. Please enter a number between 1 and {log_dict_len}.")
              
            login_count = 0
            for login in logins_dict["logins"]:
                login_count += 1
                if login_num == login_count:
                    user = login["user"]
                    key = login["password"]
                    callsign = crypt.decrypt(string=user)
                    passkey = crypt.decrypt(string=key)
                    info.session = AO3.Session(callsign, passkey)
                    info.logged_in = True