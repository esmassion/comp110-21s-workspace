"""INSERT PROJECT NAME."""

__author__ = "730189396"


def main() -> None:
    greet()


def greet() -> None:
    """Greeting the player."""
    name: str = input("What is your name: ")
    print(f"Welcome to the show {name}!")






if __name__ == "__main__":
    main()