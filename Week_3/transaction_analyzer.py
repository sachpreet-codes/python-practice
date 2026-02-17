def collect_transactions():
    transactions = {}
    for _ in range(7):
        category = str(input("Category: "))
        amount = int(input("Amount: "))
        if category not in transactions:
            transactions[category] = [amount]
        else:
            transactions[category].append(amount)
    return transactions

def analyze_transaction(data):
    total_spent = 0 
    for category in data: 
        category_total = 0       
        for amount in data[category]:
            total_spent += amount
            category_total += amount

        highest_total = None
        lowest_total = None
        highest_category = None
        lowest_category = None
        
        if highest_total == None or category_total > highest_total:
            highest_total = category_total
            highest_category = category

        if lowest_total == None or category_total <= lowest_total:
            lowest_total = category_total
            lowest_total = category

    return total_spent, highest_category, lowest_category

transactions = collect_transactions()
total, highest_cat, lowest_cat = analyze_transaction(transactions)

print("\nTotal Spent:", total)
print("Highest Spending Category:", highest_cat)
print("Lowest Spending Category:", lowest_cat)
