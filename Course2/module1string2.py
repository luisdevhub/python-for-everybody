text = "hola como estas? 959"
signo = text.find('?')
number = text[signo +1:]
number = number.strip()
value = int(number)
print(value)