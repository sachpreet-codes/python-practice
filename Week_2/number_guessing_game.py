import random

LOWER_BOUND = 1
UPPER_BOUND = 100

print(f"Guess the number between {LOWER_BOUND} and {UPPER_BOUND}")

secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
attempts = 0

while True:
    user_input = input("Enter your guess: ")

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input. Enter a number.")
        continue

    if guess < LOWER_BOUND or guess > UPPER_BOUND:
        print(f"Out of range. Guess between {LOWER_BOUND} and {UPPER_BOUND}.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
