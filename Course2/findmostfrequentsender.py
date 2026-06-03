while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("File cannot be opened:", fname)
        
count = 0
senders = dict()
for line in fh:
    if line.startswith("From:"):
        count = count + 1
        email = line.find("From:")
        sender = line[email + 5:]
        sender = sender.split()
        sender = sender[0]
        if sender not in senders:
            senders[sender] = 1
        else:
            senders[sender] = senders[sender] + 1
largest = None
largest_sender = None
for sender, count in senders.items():
    if largest is None or count > largest:
        largest = count
        largest_sender = sender
print(largest_sender, largest)
        
