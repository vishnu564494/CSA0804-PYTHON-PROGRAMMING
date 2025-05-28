import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)

print("GCD is:", gcd_abc)
