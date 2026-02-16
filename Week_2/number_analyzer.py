<<<<<<< HEAD
numbers = []

for _ in range(5):
    value = float(input("Enter Number: "))
    numbers.append(value)

largest = numbers[0]
smallest = numbers[0]
total = 0
even_count = 0
odd_count = 0

for n in numbers:
    total += n

    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 5

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average}")
print(f"Even Count: {even_count}")
print(f"Odd Count: {odd_count}")
=======
numbers = []

for _ in range(5):
    value = float(input("Enter Number: "))
    numbers.append(value)

largest = numbers[0]
smallest = numbers[0]
total = 0
even_count = 0
odd_count = 0

for n in numbers:
    total += n

    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 5

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average}")
print(f"Even Count: {even_count}")
print(f"Odd Count: {odd_count}")
>>>>>>> 8117ab818510a74a8264278ee2f28acbc02d96e8
