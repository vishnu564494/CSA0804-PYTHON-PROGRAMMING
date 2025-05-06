def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
for i in range(n - 1, 1, -1):
    if is_prime(i):
        print("Largest prime less than", n, "is", i)
        break
else:
    print("No prime number found")
