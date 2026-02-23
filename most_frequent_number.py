numbers = []

for i in range(10):
    value = int(input(f"Enter the {i+1} number: "))
    numbers.append(value)

frequency = {}

for i in numbers:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

max_count = 0
most_frequent = None

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        most_frequent = key

print(f"Most frequernt number:{most_frequent}")
print(f"Appears: {max_count}")


