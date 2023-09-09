# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic
# error.

try:
    UserIn1 = int(input("Enter 1st number: "))
    UserIn2 = int(input("Enter 2nd number: "))
    Div = UserIn1 / UserIn2
    print(Div)
except ValueError as ve:
    print("Please try different values, Only Integers: ", ve)
except ZeroDivisionError as zde:
    print("Please try different values, Zero not allowed in 2nd Input: ", zde)
