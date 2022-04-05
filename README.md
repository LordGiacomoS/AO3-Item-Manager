# AO3-Item-Manager
A WIP Python program to sort through lists of AO3 items such as works and series, and add/invite or bookmark items to collections.
The current user interface is console based, but I do intend to create a more user-friendly version once the basic program is fully functional.

# Please Note:
- I am still very new to Python, and so this program likely has several bugs, flaws, inconsistencies, and room for improvement scattered throughout.
- As of now, this program is UNFINISHED and is to be USED AT YOUR OWN RISK.
- Saving logins currently poses a slight security risk as they are only somewhat obfuscated.
- Due to the unfinished nature of the program, any github branches with the "dev" prefix are very likely to be significantly changed between versions and when being moved to a release branch, which might cause problems with any code that depends on these dev branches. However, I will try to only perform necessary changes (for efficiency, organization, and improved functionality), and document them.

# Basic Usage
An explanation of how the program is currently used.

## Types of Inputs
__Yes or No__ <br />
The first type of input the console may ask for is a yes or no answer, such as:
```
Saved login available. Would you like to use it? Y/N: █
```
To answer "Yes," put in either `Y` or `Yes`. To answer "No", put in either`N` or `No`. Once you have put in your answer, hit the enter/return key on your keyboard to send. 

__Choosing from a list__ <br />
The second type of interaction that this program uses is list based, such as:
```
1 -- Log in
2 -- Collection Items Manager (WIP) | [Requires Login]
3 -- Item List Actor (TBA) | [Limited]
4 -- Item List Exporter (TBA) | [Limited]
5 -- End Process (Automatically logs out user)
Enter your choice: █
```
To select an option from this menu, you would find the number on the left-hand side that corresponds with the option you want to pick, and type that number into the console before hitting enter, which should cause the newly selected menu to open below the previous one.


So, for example, if you were to want to go to log in, you would input `1` and hit your enter/return key, which should lead to the console look something like this:
```
1 -- Log in
2 -- Collection Items Manager (WIP) | [Requires Login]
3 -- Item List Actor (TBA) | [Limited]
4 -- Item List Exporter (TBA) | [Limited]
5 -- End Process (Automatically logs out user)
Enter your choice: 1

Enter your username or email address: █
```

__Providing a string__ <br />
The third input type used in the current menu system is a string, which is a longer sequence of text. This type of input is used for things like providing your AO3 username/email and password, or a specific link to a work, series, user, or collection.

For example, if you were to open the login menu, it would look something like this:
```
Enter your username or email address: █
```
To put provide information via this input type, you will need to type out the string and hit enter.

In this example, I would type out my username, `L_GS`, and then hit enter, which should result in the console looking something like this:
```
Enter your username or email address: L_GS
Enter your password: █
```

# Currently Implemented Menus
These menus are the ones that are currently implemented into the program.

## Main Menu
When starting the program for the first time, this is the first menu you will be presented with, and should look something like the following example.
```
Welcome, Guest. Please log in using your AO3 credentials to increase your options.
1 -- Log in
2 -- Collection Items Manager (WIP) | [Requires Login]
3 -- Item List Actor (TBA) | [Limited]
4 -- Item List Exporter (TBA) | [Limited]
5 -- End Process (Automatically logs out user)
Enter your choice: █
```
This menu is an example of a list input, and the instructions for choosing from a list explain how to interact with it.

## Login Menu
To utilize the majority of this program's features, you will need to provide it with the same login details you would use to access your archiveofourown.org account. These details will not be saved beyond your current session unless you specifically instruct the program to keep them on file.

__Username__ <br />
When opening the login menu for the first time, you should see a message along the lines of:
```
Enter your username or email address: █
```
This prompt requires you to put in the username or email address associated with your AO3 account. For more instructions, please see the entry on providing a string.


__Password__ <br />
Once you give the program your username or email address, it will ask for the password associated with the same AO3 account.
```
Enter your password: █
```
Similarly to how you entered your username or email address, you should enter your password. For more instructions, please see the entry on providing a string.

__Saving Login credentials for Future Use__ <br />
After entering both your username/email address and password, you will be asked whether you want to save your login information for future sessions with the following prompt:
```
Would you like to save this login for future sessions? (Warning, this feature is currently extremely insecure) Y/N: █
```
If you do want to save the current login for future sessions, select yes, and if not select no. See the input type entry for Yes or No for more information on how to select each option.


__Using a Saved Login__ <br />
If you have previously saved one or more logins to the system, you will be prompted with a message similar to the following when opening the login menu.

```
Saved logins available. Would you like to use one? Y/N: █
```
Selecting no will bring you to the manual login menu where you can input your username/email address and password.

If you only have one saved login, selecting yes will automatically use it.

If you have multiple saved logins, selecting yes will bring you to a selection list.

For more information, see the input type entry for Yes or No.


## Collection Items Manager:
This menu exists to use the manage items tab for collections that the current user has the authority to manage. (Documentation to be improved.)

__Set Collection ID__ <br />
This option opens a prompt to provide a string, either the url or collection ID, to identify what collection to manage.

__Set Collection Category__ <br />
This option opens a List Menu for to choose which category in the Manage Items tab of AO3 to list the items for.

__Collection Item List__ <br />
This is the main part of this section of the program, and lists the items in the specified collection category in pages. By default there will be 20 items per page, but this can be changed in the settings menu. While the item list is displayed, you can act on a specific item and send it to another category of the collection or remove it entirely.

__Return to Main Menu__ <br />
This option returns the user to the main menu.

## Settings
This menu is for managing settings that are saved between sessions of the program.

__Set Item Manager items per page__ <br />
This option is used to set the number of items listed per page of the Collection Item Manager Item List.

__Delete Saved Login Profile(s)__ <br />
This option is used to delete login profiles that have been previously saved in the login menu.

__Return to Main Menu__ <br />
This option returns the user to the main menu.


# Credits:
__Dependencies__ <br />
The library used for hiding passwords as they are typed in is <a href="https://github.com/asweigart/pwinput"> pwinput </a>, by asweigart.

A large part of the code needed to interact with AO3 uses a modified version of ArmindoFlores's unofficial <a href="https://github.com/ArmindoFlores/ao3_api"> AO3 API </a>, and so a huge thanks to everyone who has contributed to that project is in order, as this project would not exist without the foundation and insight that this api provided.

Additionally, AO3 API itself relies on a few other libraries, such as:
- <a href="https://pypi.org/project/beautifulsoup4/"> BeautifulSoup4 4.10.0 </a>; an excellent library for interpreting and navigating html and xml files using Python.
- <a href="https://github.com/lxml/lxml">lxml</a>; an efficient parsing library to help BeautifulSoup make sense of the html or xml document provided.
- <a href="https://github.com/psf/requests">requests 2.27.1</a> library, which allows for data to be sent and recieved from websites.

The other invaluable resource to this project is the website this program interacts with, <a href="https://archiveofourown.org/">archiveofourown.org</a>, and the people who keep it running, the <a href="https://www.transformativeworks.org/"> Organization for Transformative Works</a>. Without this site, this program would not exist.

# Plans
### Current Planned Menu Hierarchy:
<details><summary>Click to reveal</summary><pre><code>[Menu] Main Menu
 ├── [Section] Login Page
 │   ├── [Info] Allows program to log a person in and start an AO3 session 
 │   ├── [Variable] username/email
 │   ├── [Variable] password
 │   └── [Variable] Save login for future use?
 │
 │
 ├── [Section] Collection Manage List stuff
 │   ├── [Variable] collection ID
 │   ├── [Variable] Collection item location (Num Id)
 │   │
 │   ├── [Action Category] Common:
 │   │   ├── [Action] Remove (removes item from collection entirely)
 │   │   ├── [Action] Unreview (sends the item to Unreviewed category of Manage 
 │   │   │   Items and removes the item from public view in collection if
 │   │   │   previously approved)
 │   │   ├── [Action] Reject (sends the item to Rejected category of Manage
 │   │   │   Items, and removes the item from public view in collection if
 │   │   │   previously approved)
 │   │   └── [Action] Approve (sends the item to Approved category of Manage
 │   │       Items, and adds the item to public view in the collection, if not
 │   │       already approved)
 │   │
 │   ├── [Action Category] List Display & Navigation:
 │   │   ├── [Action] List (lists works in Manage Items category)
 │   │   │   ├── [Variable] Category (which Manage Items category to display,
 │   │   │   │   defaults to Unreviewed)
 │   │   │   ├── [Variable] start_num (work number. If none, defaults to 1.)
 │   │   │   └── [Variable] Disp amt (how many works to display per page)
 │   │   │       └── [Note] May remove this option but leave background code in 
 │   │   │           for future use
 │   │   ├── [Action] Next Page (if applicable)
 │   │   ├── [Action] Prev Page (if applicable)
 │   │   └── [Action] GoTo Page (goes to specific page number)
 │   │       └── [Variable] page number
 │   │   
 │   ├── [Sub-Section] Unreviewed
 │   │   └── [Note] use "List Display & Navigation" and "Common" except 
 │   │       Unreview
 │   ├── [Sub-Section] Invited
 │   │   └── use "List Display & Navigation" and "Common" 
 │   ├── [Sub-Section] Rejected
 │   │   └── use "List Display & Navigation" and "Common" except Reject
 │   └── [Sub-Section] Approved
 │       └── [Note] use "List Display & Navigation" and "Common" except 
 │           Approve
 │
 │
 ├── [Section] Item Actor
 │   ├── [Sub-Section] Procedural Item Actor
 │   │   ├── [Info] When given a list of urls/ids for series, works, and/or 
 │   │   │   users, this will allow a user to perform actions on the items, one
 │   │   │   by one.
 │   │   └── [Note] Use action categories in "Item Actor" module.
 │   │
 │   ├── [Sub-Section] Bulk Item Actor
 │   │   ├── [Info] When given a list of urls/ids for series, works, and/or
 │   │   │   users, this will perform an action on all of them.
 │   │   └── [Note] Use action categories in "Item Actor" module.
 │   │
 │   ├── [Action Category] Common:
 │   │   ├── [Action] subscribe
 │   │   └── [Variable] list of users/works/series to act on
 │   │
 │   ├── [Action Category] Works & Series:
 │   │   ├── [Action] bookmarking
 │   │   │   ├── [Variable] public/private bookmark
 │   │   │   ├── [Variable] rec?
 │   │   │   ├── [Variable] bookmark to collection(s)? if so which one(s)
 │   │   │   └── [Variable] bookmark notes? (and contents)
 │   │   │
 │   │   └── [Action] Downloading
 │   │       ├── [Variable] file format
 │   │       └── [Variable] Series saved in sub-folder?
 │   │
 │   ├── [Action Category] Works Specific:
 │   │   ├── [Note] see Common and Works & Series
 │   │   ├── [Action] inviting them to collections
 │   │   ├── [Action] giving kudos
 │   │   │
 │   │   └── [Note] commenting will not be action (as it would be a
 │   │       ready-made spam bot and could make AO3 mad at me for making it)
 │   │
 │   ├── [Action Category] Users:
 │   │   └── [Note] see Common
 │   │
 │   └── [Action Category] Series:
 │       └── [Note] see Common and Works & Series
 │
 │
 └── [Section] List Sorter & Exporter
     ├── [Info] Sorts through lists of series & works (i.e. Bookmarks, 
     │   collections, work lists), and exports a list of urls
     │  
     ├── [Filter Category] Common Filters:
     │   ├── [Action] filter by basic categories that AO3 natively supports
     │   └── [Action] filter by other categories
     │       ├── [Action] complete or WIP?
     │       ├── [Action] word count range
     │       │   ├── [Variable] minWordCount (if None, assume 0)
     │       │   └── [Variable] maxWordCount (if None, assume infinite)
     │       │
     │       ├── [Action] date updated range
     │       │   ├── [Variable] earliestUpdateDate (if None, assume Jan 1st,
     │       │   │   1950; required due to AO3's allowance for backdating works
     │       │   │   to accurately reflect update date)
     │       │   └── [Variable] latestUpdateDate (if None, assume tomorrow's
     │       │       date; required due to time zones making some works can
     │       │       appear updated on the day following one that user is
     │       │       actually in)
     │       │
     │       └── [Action] date posted range
     │           ├── [Variable] earliestPostDate (if None, assume Jan 1st,
     │           │   1950; required due to AO3's allowance for backdating works
     │           │   to accurately reflect post date)
     │           └── [Variable] latestPostDate (if None, assume tomorrow's
     │               date; required due to time zones making some works can
     │               appear posted on the day following one that user is
     │               actually in)
     │
     ├── [Filter Category] Bookmark Items:
     │   ├── [Note] see "Common Filters"
     │   ├── [Action] filter by other categories
     │   └── [Action] is bookmarked item series or work?
     │
     ├── [Filter Category] Work Items:
     │   └── [Note] see "Common Filters"
     │
     ├── [Filter Category] Series Items:
     │   └── [Note] see "Common Filters"
     │
     ├── [Sub-Section] Get lists from Collection
     │   ├── [Variable] Collection ID
     │   ├── [Action] Get list of Bookmarks in Collection
     │   │   └── [Note] use "Bookmark Category Filters"
     │   │
     │   └── [Action] Get list of Works in Collection
     │       └── [Note] use "Works Category Filters"
     │
     └── [Sub-Section] Get lists from User
         ├── [Variable] Username (If none, defaults to self if logged in,
         │   otherwise error.)
         ├── [Action] Get list of Works by User
         │   └── [Note] use "Works Category Filters"
         │
         ├── [Action] Get list of Series by User
         │   └── [Note] use "Series Category Filters"
         │
         └── [Action] Get list of Bookmarks of User
             └── [Note] use "Bookmarks Category Filters"
</code></pre></details>


### Other Planned/Considered Additions
#### General Changes
- Upgrade from the console-based interface to a more user friendly GUI. 
- Allow List Sorter/Exporter to work on AO3 searches (and lists of works containing a specific tag)

<details><summary>Potential Filters for List Sorter & Exporter</summary>
- author name (cannot believe AO3 doesn't allow bookmarks to be filtered by this already)<br />
- average number words per chapter (if fits within range)<br /><br />
- Certain existing AO3 category average per year (and if it fits within a certain range):<br />
  - Average Comments per year<br />
  - Average Bookmarks per year<br />
  - Average number of words per year<br />
  - Average Kudos per year<br />
  - Average subscriptions per year<br />
  - Average number of new chapters per year<br />
</details>

# Copyright Stuff
This project has a MIT license, linked <a href="https://github.com/LordGiacomoS/AO3-Item-Manager/blob/main/LICENSE">here</a>, and is, to the best of my understanding, essentially free to use for pretty much any purpose, as long as a copy of the license is attached.