import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attempts = 0
        answered_correctly = False

        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    answered_correctly = True
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            attempts += 1

        if not answered_correctly:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in (1, 2, 3):
        raise ValueError

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
