text = "X-DSPAM-Confidence:    0.8475"
space = text.find(' ')
number = text[space:]
number = number.strip()
value = float(number)
print(value)