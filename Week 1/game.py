import sys
import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

random_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue     
    except ValueError:
        continue

    if guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just Right!")
        break