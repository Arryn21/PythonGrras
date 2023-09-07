# Print Hello world
print("hello world")

"""
Data Types:
1. Numerical : 
integer: Non decimal values
float: decimal values
complex: 2+3j 
2. List : l = [1,2,"a","b"]
3. Tuple : t = (1,2,3)
4. Set : {1,2,"a"}
5. Dictionary : { "one" : 1, "two": 2 }
6. String : s = "string"
7. Boolean : TRUE, FALSE
"""

# type() function
a = 2
print(type(a), a)  # integer type

b = "string"
print(type(b), b)  # string type

# indexing
s = "abcdefg hijklmno pqrst"
print(s, "\n", s[0], s[10], s[-4])  # a j q

# Positive indexing = starts from 0
# Negative indexing = starts from -1

# slicing = to access range of characters
# syntax s[start:end+1:steps]

print(s[-1::-1])  # reverse string
print(s[5:])  # starts from 5 till end
print(s[:10])  # starts from 0 till 10

