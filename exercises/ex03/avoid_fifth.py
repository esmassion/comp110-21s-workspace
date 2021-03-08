"""EX03 - avoid_fifth function."""

__author__: str = "730189396"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("bless mothers"))
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(x: str) -> str:
    """Avoid Es function."""
    i: int = 0
    y: str = ""
    while i < len(x):
        if x[i] != "e" and x[i] != "E":
            y += x[i]
        i += 1
    return y


if __name__ == "__main__":
    main()