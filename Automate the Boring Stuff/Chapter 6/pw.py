#1 python3
import sys, pyperclip

'''
Name: Password Program
By: Zachary Stall

Description: This program is a insecure password locker

'''

PASSWORDS = {'email':   'F7minlBDDucMjuxESSKHFhTxFtjVB6',
             'blog' :   'VmALcWykaCIbvh4G83SkiksucISO34',
             'bike' :   '12345'}

if len(sys.argv) < 2:
    print('Usage: Python PW.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
