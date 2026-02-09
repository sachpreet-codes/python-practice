#This function Get numbers to do operations
def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "q":
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Try again or press Q to quit.")

#This function Get opertor to do operations
def get_operation():
    while True:
        op = input("Choose operation (+, -, *, /) or Q to quit: ").strip()
        if op.lower() == "q":
            return None
        if op in {"+", "-", "*", "/"}:
            return op
        print("Invalid operation. Choose +, -, *, /, or Q.")
        if op == "/" and num_2 == 0:
            print("Error: Division by zero is not allowed.")
            continue

#Get the user input both the numbers and operator
print("Hello welcome to Simple Calculator!!!")
print("Choose two numbers and pick your operator or Q to quit")

while True:
    num_1 = get_number("Enter First Number: ")
    if num_1 is None:
        print("Calculator Exited")
        break

    num_2 = get_number("Enter Second Number: ")
    if num_2 is None:
        print("Calculator Exited")
        break
            
    operator = get_operation()
    if operator is None:
        print("Calculator Existed")
        break

    #Perform the task provide from user inputs
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    else:
        result = num_1 / num_2
    
    print(f"Result: {result}")
    print("-" * 30)
