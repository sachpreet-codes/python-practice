number = []

for _ in range(8):
        x = int(input("Enter Number: "))
        number.append(x)

numbers = {}

for n in number:
        if n not in numbers:
            numbers[n] = 1
        else:
            numbers[n] += 1

max_count = 0
most_frequency = None

for key, value in numbers.items():
      if value > max_count:
            max_count = value
            most_frequency = key

print("Frequency:", numbers)
print("Most frequency number:", most_frequency)
print(f"Appears: {max_count} times")