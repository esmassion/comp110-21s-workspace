"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_til: int = days_to_target(population, doses, doses_per_day, target)
    #print(days_til)
    future: datetime = future_date(days_til)
    #print(future)
    print("We will reach " + str(target) + "% vaccination in " + str(days_til) + " days, which falls on " + future)

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    "Building days_to_target function."
    return int(round(2 * ((population * (target / 100) - (doses / 2)) / doses_per_day)))



def future_date(days_til: int) -> str:
    """Building future_date function."""
    today: datetime = datetime.today()
    days: str = str(days_til)
    future: datetime = today + timedelta(int(days))
    return future.strftime("%B %d, %Y")

if __name__ == "__main__":
    main()
