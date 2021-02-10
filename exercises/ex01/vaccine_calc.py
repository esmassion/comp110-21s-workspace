"""A vaccination calculator."""

__author__ = "730189396"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

# Step 1 : name and structure the input variables
population: int = int(input("Population: "))
doses_ad: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
percent_vax: int = int(input("Target percent vaccinated: "))

# Check todays date
today: datetime = datetime.today()
# print(today.strftime("%B %d, %Y"))

# Step 2: calculate the number of days until the target day based on the goal of percent vaccinated
days_til: int = int(round(2 * ((population * (percent_vax / 100) - (doses_ad / 2)) / doses_per_day)))
# print(days_til)

days: str = str(days_til)
# print(days_til)
p_vax: str = str(percent_vax)

# Step 3: Calculate the target date based on the formula for days til
future: datetime = today + timedelta(int(days))
# future: str(target_date)
# print(future)
# future = future.strftime("%B %d, %Y")
# future.strftime("%B %d, %Y")

print("We will reach " + p_vax + "% vaccination in " + days + " days, which falls on " + future.strftime("%B %d, %Y"))