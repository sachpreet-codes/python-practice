first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
third = int(input("Enter Third Number: "))

numbers = [first, second, third]

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")