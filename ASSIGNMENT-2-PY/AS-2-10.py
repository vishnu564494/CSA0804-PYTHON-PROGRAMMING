numbers = input("Enter numbers separated by space: ").split()
even_sum = 0
for num in numbers:
    if int(num) % 2 == 0:
        even_sum += int(num)
print("Sum of even numbers:", even_sum)
