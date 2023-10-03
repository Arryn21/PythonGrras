# import os

# firstfile = open("roh.txt", mode="x")
# with open("roh.txt", "w") as file:
#     file.write("Hum UP se hu!")
# with open("roh.txt", mode="r") as file:
#     print(file.read())

a = open("roh.txt", "w")
a.write("haaaaa")
a.close()
a = open("roh.txt", "r")
print(a.read())
a.close()
a= open("roh.txt","a")
a.write('tushar')
a.close()
a = open('roh.txt',"r")
print(a.read())
a.close()
with open('roh.txt',"a+") as b:
    b.write("jana tu")
    b.seek(0)
    print(b.read())



