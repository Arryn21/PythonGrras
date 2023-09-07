# Q3 write a program to accept 10 numbers from user and display the largest and smallest number
l = []
for i in range(1,11):
    num = int(input("Enter a num: "))
    l.append(i)
print("Greatest num: ", max(l))
print("Smallest num: ", min(l))

