# IMDb-in-ContextMenu
Simple program to add `Search on IMDb` to your Windows 10 Context Menu to automate the task of searching for IMDb page of a movie that you have on your computer

---
* [What is this](#what-is-this)
* [Installation](#installation)
* [FAQs](#faqs)
* [Bugs](#bugs)
* [Probable Feature Additions](#probable-feature-additions)
* [Credits](#credits)
---

## What is this
A simple program that searches for IMDb page of a movie on your computer in just a couple of clicks.  
You just need to right click on the media file of the movie and click the `Search on IMDb` button.  
A new tab will be opened on your browser and the movie's page will be searched for on IMDb.

<a href="https://ibb.co/c1PrTM6"><img src="https://i.ibb.co/yXDQsG6/Screenshot-114.png" alt="Screenshot-114" border="0"></a>

## Installation
1. Download the preferred varient from the [Download Link](https://github.com/rajdedhia10/IMDbinContextMenu/releases/)  
Check FAQs section for guidance regarging varient
2. Extract the downloaded zip file to `D:\IMDbinContextMenu`<br>
   Note: You can extract to any location you wish but you need the make changes to the **AddToRegistry.reg** and **search.bat** file
   eg. If you extract to `C:\Users\YourUsername\Downloads` then your files should look like this
   AddToRegistry.reg line 7:
   ```
   @="\"C:\\Users\\YourUsername\\Downloads\\search.bat\" \"%1\""
   ```
   search.bat line 1:  
   py method:
   ```
   python "C:\\Users\\YourUsername\\Downloads\\search.py" %1
   ```
   exe method:
   ```
   "C:\\Users\\YourUsername\\Downloads\\search.exe" %1
   ```
3. Double click on the **AddToRegistry.reg** file and follow the steps onscreen to add the registry entry
4. Done, as simple as that

## FAQs
* Why does this exist?  
A. Looking up a movie that you have on your system on IMDb in a lenghy process. This program exists to automate the process to just a couple of clicks.

* What varient should I download?  
A. Py varient if you have Python installed on your system
   exe varient if you do not have python installed on your system

* How to uninstall the program?  
A. Click on Start -> Type reg -> Press Enter on Registry Editor -> Navigate to ```HKEY_CLASSES_ROOT\*\shell\Run script``` -> Delete ```Run script```

## Bugs
* This program fails when year of the movie is enclosed in brackets
eg: ```Movie.Name.(1999).720p.10bit.mp4```

## Probable Feature Additions
Search on multiple Rating websites at once such as Metacritic, Rotten Tomatoes etc.

## Credits
[Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/) is used to convert the python file to exe files

For any doubts or suggestions you may Contact me on Telegram @[rajdedhia10](https://t.me/rajdedhia10)
