import ao3_api_collection_management.AO3 as AO3
from im_menu import info
from im_menu.errors import PageLimitError, OutOfRangeError

manage_list_category = ""
im_totalPages = ""

def collID_input():
    while(info.collection_id == ""):
        try:
            cid_input = str(input("Enter collection url or ID here: "))
            if "collections" in cid_input:
                info.collection_id = AO3.utils.collectionid_from_url(cid_input)
            else:
                info.collection_id = cid_input
        
        except:
            print("Invalid input. Please enter a valid collection id or URL")
    try:
        info.collection = AO3.Collection(info.collection_id, session=info.session)
    except:
        print("Could not locate this collection.")
            

def print_IM_menu():
    if info.collection_id == "":
        cid_locked = " [Requires Collection ID or URL]"
        cid = ""
    else:
        cid_locked = ""
    if info.collection != "":
        cid = f" [Currently: {info.collection.name}]"
    if manage_list_category != "":
        clt_cat = manage_list_category.replace("_", " ")
        clt = f" [Currently: {clt_cat.capitalize()}]"
    else:
        clt = " [Currently: None]"
  
       #ipp_current = f" [Currently {info.items_per_page}]"
      
    
    IM_menu_options = [
      f"Set Collection ID{cid}",
      f"Set Collection Category{clt}",
      f"Collection Item List{cid_locked}",
      #f"Set the number of items to display at a time.{ipp_current}",
      "Return to Main Menu"
    ]

    print("\n")
    if info.collection_id != "":
        print(f"Current Collection: \"{info.collection.name}\"")
    else:
        print("Please provide a Collection ID or URL.")
    for num, item in enumerate(IM_menu_options, 1):
        print (num, "--", IM_menu_options[num-1] )


def menu_ItemManager():
    if info.current_menu == "collection_item_home":
        while(True):
            print_IM_menu()
            option = ""
            try:
                option = int(input("Enter your choice: "))
            except:
                print("")
            #Check what choice was entered and act accordingly
            if option == 1:
                collID_input()
            elif option == 2:
                listType()
            elif option == 3:
                if info.collection is not None and manage_list_category != "":
                    list_ItemManager(manage_list_category)
                elif info.collection is not None and manage_list_category == "":
                    print("Please choose a list category.")
                    info.current_menu = "collection_item_home"
                elif info.collection is None and manage_list_category != "":
                    print("Please provide a collection ID or URL to manage.")
                    info.current_menu = "collection_item_home"
                else:
                    print("Please provide a collection ID or URL to manage and choose a list category.")
                    info.current_menu = "collection_item_home"
            #elif option == 4:
            #    from im_menu.settings_menu import save_ipp
            #    ipp_input = ""
            #    while(ipp_input == ""):
            #        try:
            #            ipp_input = int(input("Enter collection url or ID here: "))
            #            info.items_per_page = ipp_input
            #        except:
            #            print("Invalid input. Please enter a number.")
            #        save_ipp(info.items_per_page)
          
            elif option == 4:#5:
                info.current_menu = "home_nav"
                return
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

def listType():
    lt = ""
    info.current_menu = "manage_list_type"
    listType_options = [
        "Awaiting Approval",
        "Invited",
        "Rejected",
        "Approved"
    ]

    if info.current_menu == "manage_list_type":
        if lt == "":
            print("\n")
            for num, item in enumerate(listType_options, 1):
                print(num, "--", item)
        while(lt == ""):
            option = ""
            try:
                option = int(input("Enter your choice: "))
                if option < 1 or option > 4:
                    raise OutOfRangeError()
            except(TypeError, OutOfRangeError):
                print("Invalid input. Please enter a number between 1 and 4.")
            if option == 1:
                lt = "awaiting_approval"
            if option == 2:
                lt = "invited"
            if option == 3:
                lt = "rejected"
            if option == 4:
                lt = "approved"
    manage_list_category = lt


def list_ItemManager(lt, start_from=None, items_per_page=None):
    print("\n")
    info.current_menu = "list_browser"
    if items_per_page is None:
        if info.items_per_page != "":
            items_per_page = info.items_per_page
        else:
            items_per_page = 20
    if start_from is None:
        start_from = 1
  
    manage_list = info.collection._manage_items_list(info.session, lt, items_per_page, start_from)

    if isinstance(manage_list, list):
        for num, item in enumerate(manage_list, start_from):
            print(num, "--", item)
        if len(manage_list) <= 0:
            print(f"No items in this category.")
    elif isinstance(manage_list, str):
        print(manage_list)
      
    im_totalPages = info.collection._manage_items_pages(info.session, manage_list_category)
    
    page = int(((start_from-1)/items_per_page)+1)
    
    print("=============")

    if page == 1:
        pMinLim = " [Already at beginning.]"
    else:
        pMinLim = ""

    if page == im_totalPages:
        pMaxLim = " [Already at end.]"
    else:
        pMaxLim = ""
    
    if im_totalPages == 1:
        pTotalLim = " [Only 1 Page]"
    else:
        pTotalLim = ""
      

    nav_options = {
      1: f"<-- Back{pMinLim}",
      2: f"Next -->{pMaxLim}",
      3: f"Go to Page{pTotalLim}",
      4: "Act on item.",
      5: "Get Item Details",
      6: "Return to Item Manager Menu"
    }
    
    #if page == im_totalPages:
    #    nav_options.remove("Next -->")
    #elif page == 1:
    #    nav_options.remove("<-- Back")
    print(f"[Current Page: {page}/{im_totalPages}]")
  
    for key in nav_options.keys():
            print(key, "--", nav_options[key])

  
    list_option = ""
    while(list_option == ""):
        try:
            list_option = int(input("Enter your choice: "))
            if page == 1 and list_option == 1:
                raise PageLimitError("You are at the beginning.")
            if page == im_totalPages and list_option == 2:
                raise PageLimitError("You are at the end.")
        except PageLimitError as PageLimit:
                print(repr(PageLimit))
        except:
            print("Invalid input. Please enter a number between 1 and 3.")
    if list_option == 1:
        if page == 1:
            pass
        else:
            start_from = page-20
            list_ItemManager(manage_list_category, start_from)
    if list_option == 2:
        if page == im_totalPages:
            pass
            #print("You are at the end.")
        else:
            start_from = page+20
            list_ItemManager(manage_list_category, start_from)
    if list_option == 3:
        Page = ""
        while(Page == ""):
            try:
                Page = int(input("Please enter the page to go to: "))
                if Page < 1:
                    raise PageLimitError("You cannot go any further back.")
                if Page > im_totalPages:
                    raise PageLimitError("You cannot go any further forward.")
            except:
                print(f"Invalid input. Please enter a number between 1 and {im_totalPages}.")
        list_ItemManager(manage_list_category, (Page*20)-19)
    if list_option == 4:
        item_act()
        print("Action")
      
    if list_option == 5:
        print("Get item details")
      
    if list_option == 6:
        info.current_menu = "collection_item_home"
        menu_ItemManager()


def item_act():
    info.current_menu = "mi_item_act"
    item_act_item = ""
    item_act_choice = ""

    while(item_act_item == ""):
        try:
            item_act_item = int(input("Enter number of item to act on: "))
        except:
            print(f"Invalid option. Please enter a number between 1 and {im_totalPages}.")

    if manage_list_category == "awaiting_approval":
        unrv_lock = " [Already unreviewed.]"
    else:
        unrv_lock = ""
      
    if manage_list_category == "rejected":
        rjct_lock = " [Already rejected.]"
    else:
        rjct_lock = ""

    if manage_list_category == "approved" or manage_list_category == "invited":
        aprv_lock = " [Already approved.]"
    else:
        aprv_lock = ""
    
    item_act_options = {
        1: f"Unreview{unrv_lock}",
        2: f"Approve{aprv_lock}",
        3: f"Reject{rjct_lock}",
        4: "Remove",
        5: "Cancel"
    }

    for key in item_act_options.keys():
        print(key, "--", item_act_options[key])
      
    
    while(item_act_choice == ""):
        try:
            item_act_choice = int(input("Enter your choice: ")) 
        except:
            print("Invalid option. Please enter a number between 1 and 5.")
    
    if item_act_choice == 1:
        info.collection._manage_items_action(info.session, manage_list_category, item_act_item, "unreview")
        
    elif item_act_choice == 2:
        info.collection._manage_items_action(info.session, manage_list_category, item_act_item, "approve")
      
    elif item_act_choice == 3:
        info.collection._manage_items_action(info.session, manage_list_category, item_act_item, "reject")
      
    elif item_act_choice == 4:
        info.collection._manage_items_action(info.session, manage_list_category, item_act_item, "remove")
      
    elif item_act_choice == 5:
        info.current_menu = "list_browser"
        list_ItemManager()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")

#https://www.archiveofourown.org/collections/L_GSsFicRecommendations