# Check Password strength

# Conditions:
"""
Conditions
l > 8
s1 should include small letter, capital letters, 0-9 numbers !@#$%& (33,64,35,36,37,38) special characters
"""
le1 = sp1 = sm1 = ca1 = nu1 = False
password = input("Enter Your password: ")
p = password
l = len(p)
s = list(p)
s1 = []
for i in s:
    s1.append(int(ord(i)))
c = [33, 35, 36, 37, 38, 64]  # ASCII values for Special Characters !@#$%&
s1l = len(s1)

def passcheck():
    # 1st Condition Length
    def length():
        global le1
        if l > 8:
            le1 = True
        else:
            print("Too short")

    length()

    # 2nd Condition Special Characters
    def spchar():
        global sp1
        for i in s1:
            if i in c:
                sp1 = True
                break;
        if sp1 == False:
            print("Include Special Characters")

    spchar()

    # 3rd Condition Small Letters
    def smallet():
        for i in s:
            global sm1
            if i.islower():
                sm1 = True
                break;
        if not sm1:
            print("Include Small letters")

    smallet()

    # 4th Condition Capital Letters
    def caplet():
        global ca1
        for i in s:
            if i.isupper():
                ca1 = True
                break;
        if not ca1:
            print("Include Capital letters")

    caplet()

    # 5th Condition Numbers
    def nums():
        global nu1
        for i in s1:
            if 48 <= i <= 57:
                nu1 = True
                break;
        if not nu1:
            print("Include Numbers")

    nums()

    if le1 and sp1 and sm1 and ca1 and nu1:
        print("Success")

passcheck()
