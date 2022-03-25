# AO3-Item-Manager
A WIP Python program to sort through lists of AO3 items such as works and series, and add/invite or bookmark items to collections.
The current user interface is console based, but I do intend to create a more user-friendly version once the basic program is fully functional.

# Please Note:
- I am still very new to Python, and so this program likely has several bugs, flaws, inconsistencies, and room for improvement scattered throughout.
- As of now, this program is UNFINISHED and is to be USED AT YOUR OWN RISK.
- Saving logins currently poses a high security risk as they are not obfuscated or encrypted AT ALL.

# Credits:
__Dependencies__<br />
A large part of the code needed to interact with AO3 uses a modified version of ArmindoFlores's unofficial <a href="https://github.com/ArmindoFlores/ao3_api"> AO3 API </a>, and so a huge thanks to everyone who has contributed to that project is in order, as this project would not exist without the foundation and insight that this api provided.

Additionally, AO3 API itself relies on a few other libraries, such as:
- <a href="https://pypi.org/project/beautifulsoup4/"> BeautifulSoup4 4.10.0 </a>; an excellent library for interpreting and navigating html and xml files using Python.
- <a href="https://github.com/lxml/lxml">lxml</a>; an efficient parsing library to help BeautifulSoup make sense of the html or xml document provided.
- <a href="https://github.com/psf/requests">requests 2.27.1</a> library, which allows for data to be sent and recieved from websites.

The other invaluable resource to this project is the website this program interacts with, <a href="https://archiveofourown.org/">archiveofourown.org</a>, and the people who keep it running, the <a href="https://www.transformativeworks.org/"> Organization for Transformative Works </a>. Without this site, this program would not exist.

# Planned Menu Hierarchy & Front End Functionality
```
[Menu] Main Menu
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
 └── [Section] List Exporter
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
```

# Other Planned Additions
- Add an encryption system for saved logins. While it won't do much against anyone who actually knows what they are doing, it will make it slightly more difficult to just accidentally leak logins if someone is browsing through files.
