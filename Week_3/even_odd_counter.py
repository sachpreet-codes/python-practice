numbers = int(input("How many numbers do you want to enter: "))

even = 0
odd = 0

for i in range(numbers):
    x = int(input(f"Enter number {i+1}: " ))

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even: {even}")
print(f"Odd: {odd}")

