#convert elevetor floors

inp = input('European floor: ')
usf = int(inp) + 1
if usf >= 0:
        print('US floor: ', usf)
else:
        print('Enter a valid floor number')
        