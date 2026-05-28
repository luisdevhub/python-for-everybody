while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("File cannot be opened:", fname)

count = 0
for line in fh:
    if line.startswith("From:"):
        count = count + 1
        email = line.find('From:')
        sender = line[email + 5:]
        sender = sender.split()
        print(sender[0])
print("There were", count, "lines in the file with From as the first word")
