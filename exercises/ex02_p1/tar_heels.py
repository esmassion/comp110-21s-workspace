"""Tar Heels exercise redux as a structured program."""

__author__ = "730189396"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(unc: int) -> str:
    """Building tar_heels function."""
    if unc % 2 == 0 and unc % 7 == 0:
        return "TAR HEELS"
    else:
        if unc % 2 == 0:
            return "TAR"
        else:
            if unc % 7 == 0:
                return "HEELS"
            else:
                return "CAROLINA"


if __name__ == "__main__":
    main()