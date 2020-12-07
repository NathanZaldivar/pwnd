# pwnd

**Description:**

pwnd is a tool used for checking if an email is in a password breach. This tool was built using Troy Hunts Have I been pwnd? API.

**Requirements:**

in order to use this tool, you must acquire an API key from have I been pwnd Website costing US$3.50 per month.

_Link:_ https://haveibeenpwned.com/API/Key

_modules:_ The requests module is required for pwnd.

**Use:**

Syntax: python3 pwnd.py 

Files: python3 pwnd.py -f

**Installation:**

1:) install the requests module using: pip3 install requests

2:) download pwnd.py

2:) grab a API key from https://haveibeenpwned.com/API/Key and open pwnd.py with a text editor, notepad will work. You will see a dictionary with a string 'API KEY GOES HERE', replace the text inside the quotation marks with the key, save the file and close the text editor. 

4:) run and enjoy

**Module use:**

pwnd.single('random@email.com'):

searches only one email. returns a list.

pwnd.multiple(['email1@email.com', 'email2@email.com']):

multiple takes a list of emails as a parameter. returns a list.

pwnd.file('filename'):

takes a file containing emails, the format should be each email separated by a new line. returns a list.
