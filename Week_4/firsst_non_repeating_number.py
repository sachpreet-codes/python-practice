numbers = []

for i in range(5):
    value = int(input(f"Enter the {i+1} numbers: "))
    numbers.append(value)

frequency = {}

for i in numbers:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

found = False

for i in numbers:
    if frequency[i] == 1:
        print(f"Unique number: {i}")
        found = True
        break

if not found:
    print("No unique number found")