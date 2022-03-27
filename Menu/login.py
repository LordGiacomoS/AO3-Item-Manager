import os
import re
import ao3_api_collection_management.AO3 as AO3

from Menu import info

#basic log out actions
def log_out():
    info.session.logout()
    info.logged_in = False
    info.current_menu = "home_nav"

#Basic login screen
def manual_login():
    print("\n")
    callsign = ""
    passkey = ""
    save_login = ""
      
    while(callsign == ""):
        try:
            callsign = str(input("Enter your username or email address: "))
        except:
            print("Invalid input.")
    while(passkey == ""):
        try:
            passkey = str(input("Enter your password: "))
        except:
            print("Invalid input.")
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
            s_l_string = str(input("Would you like to save this login for future sessions? (Warning, this feature is currently extremely insecure) Y/N: "))
            if re.search(info.Yes, s_l_string) is not None:
                save_login = True
            elif re.search(info.No, s_l_string) is not None:
                save_login = False
            else:
                print("Invalid Input. Please enter \"Yes\" or \"No\".")
        except:
            print("Invalid Input. Please enter \"Yes\" or \"No\".")
     
    if passkey is not None and callsign is not None and save_login is not None:
        if save_login == False:
            info.logged_in = True

        if save_login == True:
            with open(f"Logins/{callsign}.txt", "w") as f:
                f.writelines([callsign, "\n", passkey])
            info.logged_in = True
    info.current_menu = "home_nav"

#Login Code for saved logins:
def useSavedLogins():
    if checkSavedLogins() is not None:
        use_saved_login = ""
        while(use_saved_login == "" and checkSavedLogins() == 2):
            try:
                if checkSavedLogins == 2:    
                    usl_string = str(input("Saved login available. Would you like to use it? Y/N: "))
                if re.search(info.Yes, usl_string) is not None:
                    use_saved_login = True
                elif re.search(info.No, usl_string) is not None:
                    use_saved_login = False    
            except:      
                print("Invalid Input. Please enter \"Yes\" or \"No\".")

        while(use_saved_login == "" and checkSavedLogins() > 2):
            try:
                if checkSavedLogins() > 2:    
                    usl_string = str(input("Saved logins available. Would you like to use one? Y/N: "))
                if re.search(info.Yes, usl_string) is not None:
                    use_saved_login = True
                elif re.search(info.No, usl_string) is not None:
                    use_saved_login = False    
            except:      
                print("Invalid Input. Please enter \"Yes\" or \"No\".")
    return use_saved_login

def checkSavedLogins():
    directory = os.getcwd() + "/Logins"
    if len(os.listdir(directory)) >= 2:
        cl_available = len(os.listdir(directory))
    else:
        cl_available = None
    return cl_available
  
def savedLoginsMenu():
    directory = os.getcwd() + "/Logins"
    login_to_use = ""
    callsign = ""
    passkey = ""
    if len(os.listdir(directory)) == 2:
        file = os.listdir(directory)[1]
        with open(directory + "/" + file, "r") as f:
            callsign = re.sub("\n", "", f.readline())
            passkey = f.readline()
        #print(callsign, passkey)
    if len(os.listdir(directory)) > 2:
        count = 1
        #print(enumerate(os.listdir(directory)))
        #if count <= len(os.listdir(directory)[1]):
        for num, login in enumerate(os.listdir(directory)[1], 1):
            if count < len(os.listdir(directory)):
                login = os.listdir(directory)[count].replace(".txt", "")
                print(num, "--", login)
            count += 1
        login_num = ""
        while login_to_use == "":
            try:
                login_num = int(input("Enter your choice: "))
            except:
                print("Wrong input. Please enter a number ...")
            login_to_use = os.listdir(directory)[login_num]
        file = f"{directory}/{login_to_use}"
        with open(file, "r") as f:
            callsign = re.sub("\n", "", f.readline())
            passkey = f.readline()
            #print(callsign, passkey)
    info.session = AO3.Session(callsign, passkey)
    info.logged_in = True
    info.current_menu = "home_nav"