import os
import re
import ao3_api_collection_management.AO3 as AO3
from Menu import info

info.current_menu = "home_nav"

#Login Code for cached logins...
directory = os.getcwd() + "/Logins"
print(directory)
if len(os.listdir(directory)) >= 1:
    use_saved_login = ""
    login_to_use = ""
    while(use_saved_login == ""):
        try:
            if len(os.listdir(directory)) == 1:    
                usl_string = str(input("Cached login available. Would you like to use it? Y/N: "))
            if len(os.listdir(directory)) > 1:    
                usl_string = str(input("Cached logins available. Would you like to use one? Y/N: "))
            if usl_string == "Y":
                use_saved_login = True
            elif usl_string == "N":
                use_saved_login = False    
        except:      
            print("Invalid Input")
    if use_saved_login is True:
        callsign = ""
        passkey = ""
        if len(os.listdir(directory)) == 1:
            file = os.listdir(directory)[0]
            with open(directory + "/" + file, "r") as f:
                callsign = re.sub("\n", "", f.readline())
                passkey = f.readline()
            #print(callsign, passkey)
        if len(os.listdir(directory)) > 1:
            count = 1
            for login in os.listdir(directory):
                login = os.listdir(directory)[count]
                count += 1
            for num, login in enumerate():
                print(num, "--", login)

            login_num = ""
            while login_to_use == "":
                try:
                    login_num = int(input("Enter your choice: "))
                except:
                    print("Wrong input. Please enter a number ...")
                login_to_use = os.listdir(directory)[login_num]
            file = login_to_use
            with open(file, "r") as f:
                callsign = f.readline()
                passkey = f.readline()
                print(callsign, passkey)
        session = AO3.Session(callsign, passkey)
        info.logged_in = True
          
if info.logged_in == True:
    print("\n")
    print(f"Welcome, {session.user}")
    
    
menu_options = {
    1: "Login (Working)",
    2: "Collection Items Manager (WIP)",
    3: "Item List Actor (TBA)",
    4: "Item List Exporter (TBA)",
    5: "End Process"
}

def print_menu():
    for key in menu_options.keys():
        print (key, "--", menu_options[key] )

def GoToLogin():
#login code for new sessions
    info.current_menu = "login"
    if info.logged_in is False:
        callsign = ""
        passkey = ""
        save_login = ""
      
        while(callsign == ""):
            try:
                callsign = str(input("Enter your username or email address: "))
            except:
                print("Invalid input...")
        while(passkey == ""):
            try:
                passkey = str(input("Enter your password: "))
            except:
                print("Invalid input...")
        
        while(save_login == ""):
            try:
                s_l_string = str(input("Would you like to save this login for future sessions? (Warning, this feature is currently extremely insecure) Y/N: "))
                if s_l_string == "Y":
                    save_login = True
                elif s_l_string == "N":
                    save_login = False
            except:
                print("Invalid input...")
              
        if passkey is not None and callsign is not None and save_login is not None:
            if save_login == False:
                session = AO3.Session(callsign, passkey)
                info.logged_in = True

            if save_login == True:
                with open(f"Logins/{callsign}.txt", "w") as f:
                    f.writelines([callsign, "\n", passkey])
                session = AO3.Session(callsign, passkey)
                info.logged_in = True

    print("\n")
    print(f"Welcome, {session.user}")

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
            print("Wrong input. Please enter a number ...")
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
            print("Thank you for using L_GS\'s AO3 Item Manager.")
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 5.")