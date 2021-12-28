from requests import get
import pyperclip

ipv4 = get('https://api.ipify.org').text
ipv6 = get('https://api64.ipify.org').text

print('IPv4 address:    {}'.format(ipv4))
print('IPv6 address:    {}'.format(ipv6))
print('Do you want to copy your IP? Press any other key to close the program.')
print('1: IPv4  2: IPv6')

while True:
    try:
        copyip = int(input())
        if copyip == 1:
            pyperclip.copy(ipv4)
        elif copyip == 2:
            pyperclip.copy(ipv6)
    except:
        copyip != (1, 2)
        break