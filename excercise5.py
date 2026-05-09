largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num1 = int(num)
    except ValueError:
        print("Invalid input")
        continue
    if largest is None or num1 > largest:
        largest = num1
    if smallest is None or num1 < smallest:
        smallest = num1
print("Maximum is", largest)
print("Minimum is", smallest)