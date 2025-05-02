n = 6
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("Fibonacci:", fib[:n])
