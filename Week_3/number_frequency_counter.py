numbers = []

for i in range(10):
    value = int(input(f"Enter {i+1} Number: "))
    numbers.append(value)

frequency = {}

for i in numbers:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1 

print("Numbers entered:", numbers)
print("Frequency:")
for key, value in frequency.items():
    print(f"{key} = {value}")

