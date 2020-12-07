#! /usr/bin/python3
import requests
import sys
import re
import time

api = {'hibp-api-key': 'API KEY GOES HERE'}
email = sys.argv

#api call
def single(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        time.sleep(1.6) # rate limit
        r = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/{}'.format(email), headers=api)
        if r.text != '':
            return [f'Email {email} found in {x} breach' for x in r.text.replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('"', '').replace('Name:', '').split(',')]
    else:
        return 'invalid email'



#multiple api calls
def multiple(email):
    breach = []
    ERROR = []
    for i in email:
        if re.match(r'[^@]+@[^@]+\.[^@]+', i):
            time.sleep(1.6) # rate limit
            r = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/{}'.format(i), headers=api)
            if r.text != '':
                breach.extend([f'Email {i} found in {x} breach' for x in r.text.replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('"', '').replace('Name:', '').split(',')])
        else:
            ERROR.append('invalid email for option: {}'.format(i))
            continue
    breach.extend(ERROR)
    return breach


#api call for files
def file(email):
    try:
        ERROR = []
        breach = []
        with open(email) as emails:
            for y in emails.readlines():
                i = y.strip()
                if re.match(r'[^@]+@[^@]+\.[^@]+', i):
                    time.sleep(1.6) # rate limit
                    r = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/{}'.format(i), headers=api)
                    if r.text != '':
                        breach.extend([f'Email {i} found in {x} breach' for x in r.text.replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('"', '').replace('Name:', '').split(',')])
                else:
                    ERROR.append('invalid email for option: {}'.format(i))
                    continue
        breach.extend(ERROR)
        return breach
    except FileNotFoundError:
        return 'File not found'

def api_check():
    r = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/randomemail@email.com', headers=api)
    if '"statusCode": 401' in r.text:
        raise Exception('Invalid Api key!')


def main():
    if len(email) == 1:
        print('Syntax: pwnd <email> <email2> <email3>\nFiles: pwnd -f <file path>')
    elif '-f' in email:
        breaches = file(email[2])
        if isinstance(breaches, list):
            for i in breaches:
                print(i)
        else:
            print(breaches)
    elif len(email) > 2:
        breaches = multiple(email[1:])
        if isinstance(breaches, list):
            for i in breaches:
                print(i)
        else:
            print(breaches)
    else:
        breaches = single(email[1])
        if isinstance(breaches, list):
            for i in breaches:
                print(i)
        else:
            print(breaches)

    quit()


api_check()

if __name__ == '__main__':
    main()
