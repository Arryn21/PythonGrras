# Write a Python program to create a decorator to convert the return value of a function
# to a specified data type.

def decorator(funcCall):
    def chgdatatype(ValueCall):
        funcCall(ValueCall)
        updatedDatatype = int(ValueCall)
        print("Data Type After: ", type(updatedDatatype), updatedDatatype)
        # return updatedDatatype

    return chgdatatype


@decorator
def func1(Value1):
    print("Data Type Before: ", type(Value1), Value1)
    return Value1


UserIn = input("Enter Value: ")
print(func1(UserIn))
