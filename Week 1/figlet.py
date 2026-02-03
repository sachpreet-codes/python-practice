import sys
import random
import pyfiglet


def main():
    fonts = pyfiglet.FigletFont.getFonts()
    args = sys.argv[1:]

    if len(args) == 0:
        font = random.choice(fonts)
    elif len(args) == 2:
        if args[0] not in ["-f", "--font"]:
            sys.exit("Error: Invalid flag")

        if args[1] not in fonts:
            sys.exit("Error: Invalid font")

        font = args[1]
    else:
        sys.exit("Error: Invalid number of arguments")

    text = input("Input: ")

    figlet = pyfiglet.Figlet(font=font)

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
