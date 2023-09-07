# Q5 Accept the age , gender ('M','F'), number of days and display the wages
# Age >= 18 and <30 wages will be 700 for male , Age>=30 and <40 wages will be 800 for female
Age = int(input("Enter your age: "))
Gender = input("Enter your gender (M, F): ")
Days = int(input("Enter no. of days you worked: "))

a = Age
g = Gender
d = Days

if g=="M" or g=="m":
    if a>=18 and a<30:
        print("Your wages: ", 700*d)
    else:
        print("Kon ho tum bhai!!!")
elif g=="F" or g=="f":
    if a>=30 and a<40:
        print("Your wages: ", 800*d)
    else:
        print("Kon ho tum bhai!!!")
else:
    print("Kon ho tum bhai!!!")