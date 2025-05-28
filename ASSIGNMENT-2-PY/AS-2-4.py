import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Real and distinct roots:", r1, "and", r2)
elif d == 0:
    r = -b / (2*a)
    print("Real and equal roots:", r, "and", r)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex roots:", f"{real}+{imag}i and {real}-{imag}i")
