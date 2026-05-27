while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("File cannot be opened:", fname)
        
total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    number = line.find(':')
    number = line[number + 1:]
    number = number.strip()
    value = float(number)
    total = total + value
    count = count + 1
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No valid lines found.")