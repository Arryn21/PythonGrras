"""
Operators: 7 Types
1) ASSIGNMENT --> = , += , -= , *= ,...
2) ARITHMETIC --> +,-,*,/,//,%,**
3) LOGICAL --> and or not
4) COMPARISON --> == , < , > , <= , >=
5) MEMBERSHIP --> in , not in
6) IDENTITY --> is , is not
7) BITWISE --> and(&) , or(|) , ex-or(^)
"""

# arithmatic operators
print("Add: 1 + 3 = ", 1 + 3)
print("Sub: 10 - 3 = ", 10 - 3)
print("Mul: 6 * 3 = ", 6 * 3)
print("Div: 5 / 2 = ", 5 / 2)
print("Floor div: 5 // 2 = ", 5 // 2)
print("Power: 2 ** 3 = ", 2 ** 3)
print("Modulo: 5 % 2 = ", 5 % 2)
print("To get unit digit: 109 % 10 = ", 109 % 10)

# assignment operators
a = 9
print(a)
a += 10
print(a)
a -= 5
print(a)

# Comparison operator

print(12 == 12)
print(12 == 33)
print(34 >= 4)

# Logical operator

a = 3
b = 10
print(a < b and a <= b)
print(a > b and a <= b)
print(a > b or a <= b)
print(not (a > b or a <= b))

# Membership operator --> in, not in

l1 = [1, 2, 3, "apple"]
print("apple" in l1)
print(3 not in l1)
t2 = (1,2,3)
print(3 in t2)
