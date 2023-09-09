# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does
# not exist.

ListIn = [1, 2, "abc", 6, 7]
try:
    ListIn.add(8)
    print(ListIn)
except AttributeError as ae:
    print("What attribute are you using bruh! : ", ae)
