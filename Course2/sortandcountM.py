while True:
    name = input("Enter file:")
    try:
        fn = open(name)
        break
    except:
        print("File cannot be opened:",name)
countH = 0
hours = dict()
for line in fn:
    if line.startswith("From ") and not line.startswith("From:"):
        countH = countH + 1
        colon = line.find(':')
        hour = line[colon - 2:colon]
        hour = hour.split()
        if hour[0] not in hours:
            hours[hour[0]] = 1
        else:
            hours[hour[0]] = hours[hour[0]] + 1

for hour, countH in sorted(hours.items(), reverse=False):
    print(hour, countH)