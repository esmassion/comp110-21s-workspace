"""EX03 - prime functions."""

__author__: str = "730189396"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(5))
    print(is_prime(6))
    print(is_prime(7))
    print(list_primes(10, 20))


def is_prime(x: int) -> bool:
    """Is it prime function."""
    y: int = 2
    if x < 2:
        return False
    else:
        while y <= (x // 2):
            if x % y == 0:
                return False
            y += 1
        return True


def list_primes(x: int, y: int) -> list[int]:
    """Primes between ints."""
    i: int = x
    output: list[int] = []
    while i < y:
        if is_prime(i):
            output.append(i)
        i += 1
    return output


if __name__ == "__main__":
    main()