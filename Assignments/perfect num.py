# Q1 Write a program to accept a number and check whether it is a perfect number or not
num = int(input("Enter a number: "))
l = []
for i in range(1, num):
    if num % i == 0:
        l.append(i)
s = sum(l)

if s==num:
    print("Yes Its a Perfect Num")
else:
    print("No Its not")
