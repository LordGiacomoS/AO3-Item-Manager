# Basic Usage
### Types of Inputs
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


## Specific Menus
__Main Menu__ <br />
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

__Login Menu__ <br />
To utilize the majority of this program's features, you will need to provide it with the same login details you would use to access your archiveofourown.org account. These details will not be saved beyond your current session unless you specifically instruct the program to keep them on file.

##### Username <br />
When opening the login menu for the first time, you should see a message along the lines of:
```
Enter your username or email address: █
```
This prompt requires you to put in the username or email address associated with your AO3 account. For more instructions, please see the entry on providing a string.


##### Password <br />
Once you give the program your username or email address, it will ask for the password associated with the same AO3 account.
```
Enter your password: █
```
Similarly to how you entered your username or email address, you should enter your password. For more instructions, please see the entry on providing a string.


##### Saving Login credentials for Future Use <br />
After entering both your username/email address and password, you will be asked whether you want to save your login information for future sessions with the following prompt:
```
Would you like to save this login for future sessions? (Warning, this feature is currently extremely insecure) Y/N: █
```
If you do want to save the current login for future sessions, select yes, and if not select no. See the input type entry for Yes or No for more information on how to select each option.


##### Using a Saved Login <br />
If you have previously saved one or more logins to the system, you will be prompted with a message similar to the following when opening the login menu.

```
Saved logins available. Would you like to use one? Y/N: █
```
Selecting no will bring you to the manual login menu where you can input your username/email address and password.

If you only have one saved login, selecting yes will automatically use it.

If you have multiple saved logins, selecting yes will bring you to a selection list.

For more information, see the input type entry for Yes or No.