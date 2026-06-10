import re

while True:
    file = input('Enter file name: ')
    try:
        fh = open(file)
        break
    except:
        print('File cannot be opened:', file)
numlist = list()
for line in fh:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) < 1:
        continue
    for num in stuff:
        num = int(num)
        numlist.append(num)
print(sum(numlist))