# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs
# are not numerical.

# We cannot get a TypeError Exception by getting input from user as we will convert the input, and it will always
# show as ValueError

# try:
#     UserIn = int(input("Enter an Integer: "))
#     print(UserIn)
# except ValueError as ve:
#     print("It's not an Integer", ve)

Value1 = 3
Value2 = "three"
print(f"Value1 = {Value1} \n"
      f"Value2 = {Value2}")
try:
    print(Value1 + Value2)
except TypeError as te:
    print("You cannot just add two different types of Values.", te)
