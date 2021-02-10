"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730189396"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


fortune: int = randint(1, 4)


def fortune_cookie() -> str:
    """Building fortune_cookie function."""
    if fortune == 1:
        return "Eat with the ones you cook with."
    else:
        if fortune == 2:
            return "If you're gonna be bad, be good at it."
        else: 
            if fortune == 3:
                return "JUST DO IT."
            else: 
                return "Take what you can and give nothing back."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
