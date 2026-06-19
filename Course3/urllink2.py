import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


print("firsturl", url)
for i in range(count):
    tags = soup('a')
    tag = tags[position-1]
    print('Retrieving:', tag.get('href', None))
    url = tag.get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()  
    soup = BeautifulSoup(html, 'html.parser')
print('Last Url:', url)
