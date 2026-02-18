number = int(input("How many numbers: "))

total = 0

for n in range(number):
    value = int(input(f"Enter number {n+1}: "))

    if n == 0:
        total = value
        largest = value
        smallest = value
    else:
        total += value

        if value > largest:
            largest = value

        if value < smallest:
            smallest = value

print(f"Total: {total}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
   



    
    
    
                               