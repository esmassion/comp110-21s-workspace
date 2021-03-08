"""EX03 - palindromify function."""

__author__: str = "730189396"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(x: str, b: bool) -> str:
    """Palindrom function."""
    y: str = x
    if b:
        i: int = len(y) - 1
    else:
        i = len(y) - 2
    while i >= 0:
        y += y[i]
        i -= 1
    return y


if __name__ == "__main__":
    main()