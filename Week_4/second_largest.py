numbers = []

for i in range(10):
    value = int(input(f"Enter the {i+1} number: "))
    numbers.append(value)

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest:
        if second_largest is None or num > second_largest:
            second_largest = num

print(f"The decond largest number is {second_largest}")

