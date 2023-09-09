# Write a Python program to filter a given list to determine if the values in the list
# have a length of 6 using Lambda.
# Sample Output:
# Monday
# Friday
# Sunday

Days_List = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

checkLen = lambda x, i: len(x[i]) == 6

for j in range(len(Days_List)):
    result = checkLen(Days_List, j)
    if result:
        print(Days_List[j])