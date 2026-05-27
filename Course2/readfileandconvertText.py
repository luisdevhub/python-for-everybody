while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("File cannot be opened:", fname)
for line in fh:
    print(line.upper().rstrip())   