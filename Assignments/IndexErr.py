# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out
# of range.

List1 = [1, 2, 3, "abc", "def", 4, 5]
print(f"List: {List1}")
try:
    UserIn = int(input("Enter an Index Number to print: "))
    print(f"Value at index {UserIn} is {List1[UserIn]}")
except IndexError as ie:
    print("Wrong Index: ", ie)
