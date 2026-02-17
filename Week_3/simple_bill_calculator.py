price = float(input("Price: "))
quantity = int(input("Quantity: "))

total_cost = price * quantity

if total_cost >= 1000:
    discount = (total_cost * 10) / 100
else:
    discount = 0

discounted_price = total_cost - discount

print(f"Total: {total_cost}")
print(f"Discount: {discount}")
print(F"Final: {discounted_price}")