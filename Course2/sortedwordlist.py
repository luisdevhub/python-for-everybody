while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("File cannot be opened:", fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))