hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    over_rate = r * 1.5
    over = h - 40
    base = 40 * r
    calculation_over = over * over_rate
    final_rate = base + calculation_over
    print(final_rate)
else:
    normal_rate = h * r
    print(normal_rate)