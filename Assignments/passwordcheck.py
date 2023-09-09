# Check Password strength

# Conditions:
"""
Conditions
l > 8
s1 should include small letter, capital letters, 0-9 numbers !@#$%& (33,64,35,36,37,38) special characters
"""

password = input("Enter Your password: ")
p = password
l = len(p)
s = list(p)
s1 = []
for i in s:
    s1.append(int(ord(i)))
c = [33, 35, 36, 37, 38, 64]  # ASCII values for Special Characters !@#$%&
s1l = len(s1)
count = 0


def passcheck():
    plus = 0
    # 1st Condition Length
    def length():
        if l < 8:
            print("Too short")

    length()

    # 2nd Condition Special Characters
    def spchar():
        k = count
        for i in s1:
            if i not in c:
                k += 1
            if k == s1l:
                print("Include Special Characters")

    spchar()

    # 3rd Condition Small Letters
    def smallet():
        k = count
        for i in s:
            if not i.islower():
                k += 1
            if k == s1l:
                print("Include Small letters")

    smallet()

    # 4th Condition Capital Letters
    def caplet():
        k = count
        for i in s:
            if not i.isupper():
                k += 1
            if k == s1l:
                print("Include Capital letters")

    caplet()

    # 5th Condition Numbers
    def nums():
        k = count
        for i in s1:
            if 48 >= i or i >= 57:
                k += 1
            if k == s1l:
                print("Include Numbers")

    nums()


passcheck()
