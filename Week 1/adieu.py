def format_names(names):
    n = len(names)

    if n == 1:
        return names[0]
    elif n == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


def main():
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    result = format_names(names)
    print(f"Adieu, adieu, to {result}")


if __name__ == "__main__":
    main()