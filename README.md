ITCS
====

+ **Project URL**
https://github.com/hszcg/ITCS

Including Content Management Tools and HTML Auto-generation Tools from JSON data files.


## Required Libs:
* Python 2.7
* PyQt4


## Content Management Tools
+ **Directory**
gui/

+ **Usage**
'''
$ cd gui/
$ python window.py 
'''

+ **Operations**
* On initialization, program will automatically load data from "gui/data.json".
* Use "Add/Delete" button to add/delete items.
* Use "Up/Down/Top/Bottom" button to reorder items.
* Use "Save Item" button to save current item to data memmory.
* Use "Save File" button to save current data to "gui/data.json", while the old one is backup to "gui/data.json.bak".


## Data
+ **Data File**
gui/data.json 

+ **Data Format**
JSON Format, Level 1 key is 


## Deploy
Copy the "html/" directory to host dir.


## Backup
+ **Data Backup**
Data is automatically backup from "gui/data.json" to "gui/data.json.bak"

+ **HTML Backup**
HTML is backup from "html/" to "html_bak/"
'''
$ ./backup.sh 
'''


## Others
* 'counter' is reserved for additional Javascript code in each HTML page

