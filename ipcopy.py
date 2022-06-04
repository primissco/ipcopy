from requests import get
import pyperclip

type = int(input("Which type? (4/6): "))

if type == 4:
    ip = get('https://api.ipify.org').text
    print('IPv4 address:    {}'.format(ip))
    pyperclip.copy(ip)
elif type == 6:
    ip = get('https://api64.ipify.org').text
    print('IPv4 address:    {}'.format(ip))
    pyperclip.copy(ip)
else:
    print("Wrong input. Only '4' and '6' acceptable. Please try again.")
