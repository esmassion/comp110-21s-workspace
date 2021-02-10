"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730189396"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = randint(1, 4)

if fortune == 1:
    print("Eat with the ones you cook with.")
else:
    if fortune == 2:
        print("If you're gonna be bad, be good at it.")
    else: 
        if fortune == 3:
            print("JUST DO IT.")
        else: 
            print("Take what you can and give nothing back.")

print("Now, go spread positive vibes!")