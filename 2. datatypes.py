# Functions / Methods to use on different data types
# from typing import List

"""
Data Types: 7 Types
1. Numerical :
    integer: Non-decimal values
    float: decimal values
    complex: 2+3j
2. List : l = [1,2,"a","b"]
3. Tuple : t = (1,2,3)
4. Set : {1,2,"a"}
5. Dictionary : { "one" : 1, "two": 2 }
6. String : s = "string"
7. Boolean : TRUE, FALSE
"""

### String --> with index

s = "helooo how do u do it? "
# print(s)
# print(s.strip())  # eliminates blank spaces around the string
#
# print(s.split("o"))  # splits the string where ever "o" occurs
# print(s.upper())  # all caps
# print(s.lower())  # all small
# print(s.title())  # all first letters caps
# print(s.capitalize())  # only first letter caps

### Lists are Orderable and Mutable

l: list[int | str] = [1, 2, 3, "a", "b", "chango"]
print(l)
l.append("harry")  # adds new value at the end of the list
# print(l)
l.insert(3, 456)  # adds new value at specified index
# print(l)
l.pop()  # removes last value
# print(l)
l.pop(5)  # removes value at index 5
# print(l)
l.remove(456)  # removes that exact value
# print(l)
l.clear()  # removes everything
# print(l)
del l  # deletes that variable
# print(l)  # now this will show error

l2 = [11, 2, 23, 3, 4]
l2.sort()  # sorts the list
# print(l2)
l2.sort(reverse=True)  # reverse sorting
# print(l2)
l1 = [99, 88, 77, 66]
l1.extend(l2)  # l1 + l2
# print(l1)
l3 = [[1, 2], [3, 4]]  # list inside a list
# print(l3[0][1])

### Tuple = Orderable and Immutable -> cannot be changed once created

t1 = (1, 2, 3, "abc", 89.99)
print(t1[0])

### SET --> UNORDERABLE , MUTABLE , NO duplicate

s1 = {1, 2, 3, "abc"}
# print(s1[0]) # will show error as set has no index
s1.add(87)
print(s1)
s2 = {1, 2, 3, 1, 2, 3, "def", 678}
print(s2)  # it only takes unique values
print(s1.intersection(s2))  # prints only common values from both sets
print(s1.union(s2))  # prints all the unique values from both sets
s1.clear()
print(s1)
del s1

### Dictionary --> "key" : Value

d1 = {"name": "vishal", "age": 24}
print(d1)  # {'name': 'vishal', 'age': 24}
print(d1.items())  # dict_items([('name', 'vishal'), ('age', 24)])
print(d1.keys())  # dict_keys(['name', 'age'])
print(d1.values())  # dict_values(['vishal', 24])
d1.update({"location": "ahmedabad"})
print(d1)
print(d1['location'])
print(d1.popitem())
d1.update({"birthmonth": "April"})
print(d1)
print(d1.pop("birthmonth"))
print(d1)

### BOOLEAN --> True, False

a = True
print(type(a))
print(12 > 5)
print(5 > 12)
