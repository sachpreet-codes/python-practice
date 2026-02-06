import sys


def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit()

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit()

    try:
        with open(filename) as file:
            count = 0
            for line in file:
                stripped = line.lstrip()

                if stripped.strip() == "":
                    continue

                if stripped.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit()


if __name__ == "__main__":
    main()