# pwnd

**Description:**
pwnd is a tool used for checking if an email is in a password breach. This tool was built using Troy Hunts Have i been pwnd? API.


**Requirements:**

in order to use this tool you must aquire a API key from have i been pwnd Website costing US$3.50 per month.

_Link:_ 
https://haveibeenpwned.com/API/Key

_modules:_
The requests module is required for pwnd.


**Use:**

Syntax: python3 pwnd.py <email1> <email2> <email3>
Files: python3 pwnd.py -f <file path>
 


**Installation:**
1:)
install the requests module using: pip3 install requests

2:)
download pwnd.py and run

**Module use:**

pwnd.single('random@email.com'):

searches only one email. returns a list.

pwnd.mutiple(['email1@email.com', 'email2@email.com']):

mutiple takes a list emails as a parameter. returns a list.

pwnd.file('file name'):

takes a file containing emails, the format should be each email sepreated by a new line. returns a list.
