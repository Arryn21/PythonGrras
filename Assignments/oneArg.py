# Write a Python program to create a function that takes one argument, and that argument will be multiplied with
# an unknown given number.

import random


def InputFunc(InputArg):
    unKnownNum = random.randint(1, 10)
    Mult = InputArg * unKnownNum
    return Mult


UserIn = int(input("Provide a Num: "))
result = InputFunc(UserIn)
print(f"Your_number * Unknown_number = {result}")
