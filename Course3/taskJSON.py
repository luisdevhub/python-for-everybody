import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
info = json.loads(data)

nums = list()
comments = info['comments']

for item in comments:
    count = int(item['count'])
    nums.append(count)


print('Count:', len(nums))
print('Sum:', sum(nums))
    
